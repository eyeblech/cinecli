{
  description = "Nix flake for the cinecli Python CLI";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { self, nixpkgs, ... }:
    let
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      forAllSystems =
        f:
        builtins.listToAttrs (
          map (system: {
            name = system;
            value = f system;
          }) systems
        );

    in
    {
      packages = forAllSystems (
        system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
        {
          cinecli = pkgs.python3Packages.buildPythonPackage {
            pname = "cinecli";
            version = "flake";
            src = self;

            propagatedBuildInputs = with pkgs.python3Packages; [
              requests
              rich
              typer
            ];

            pyproject = true;
            build-system = with pkgs.python3Packages; [
              setuptools
              wheel
            ];

          };

          default = self.packages.${system}.cinecli;
        }
      );
    };
}
