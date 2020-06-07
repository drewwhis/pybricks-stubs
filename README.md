# pybricks-stubs

## Package Rationale

This package is meant to provide typings (and IntelliSense) to those developing Python programs for the LEGO&reg; MINDSTORMS&reg; EV3 with the official LEGO&reg; software ([pybricks](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3)).

This package does not support executing robot code on the computer or on the robot. This package does provide type hinting while writing Python code on the computer for later upload/deployment to the robot.

## Version Documentation

For version 1.0.0 and earlier, all typings are based on the [LEGO&reg; API 1.0.0](https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/ev3micropythonv100-71d3f28c59a1e766e92a59ff8500818e.pdf).

For versions after 1.0.0 (including a final 2.0.0 and the 1.0.* pre-releases for 2.0.0), all typings are based on the [LEGO&reg; API 2.0.0](https://pybricks.github.io/ev3-micropython/).

## Choosing Your Version

For the latest version, you can run:

`pip install pybricks-stubs`

If you are working with version 1.0.0 from LEGO&reg;, make sure you install version 1.0.0 of the package with this command:

`pip install pybricks-stubs==1.0.0`

## Turning On Type Hints

If you are working with version 2.0.0 or later and have generated a project using the Visual Studio Code extension, you may need to edit your settings file in order for your hints to work.

If so, you would go to the .vscode folder to the settings.json file. You will want to edit this line:

    "python.languageServer": "None"

Just change "None" to "Microsoft" or "Jedi" (either should work). You will have to reload the project. Follow the prompts or close Visual Studio Code and re-open the project.

Be aware that things your computer lets you import may not be available on the EV3's local version of Python. Make sure you check that your code runs on the brick whenever you `import` something new.

## Disclaimer

This package is **not** produced or maintained by LEGO&reg;, nor is it officially endorsed by LEGO&reg; or *FIRST*&reg;.

## Issues

Please report any issues you encounter on the GitHub page.
