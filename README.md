# Info

Super+Alt+0: Cycle up
Super+Alt+9: Cycle down

Alternatively, you can switch themes via Super+Shift+P and fuzzy search, e.g. "Super+Shift+P qtn" for next theme, "Super+Shift+P qtp" for previous theme.

Best to configure it to match your environments in:

`Preferences -> Package Settings -> QuickThemes -> Settings - User`

Example configuration with two modes to harmonize with ambient light:

    {
        "quick_themes_selection": 1,
        "quick_themes_defaults":
        {
            "color_scheme": "Packages/Color Scheme - Default/Solarized (Dark).tmTheme",
            "font_face": "Source Code Pro Light",
            "font_size": 12
        },
        "quick_themes":
        [
            {}, // use defaults
            {
                "color_scheme": "Packages/Color Scheme - Default/Solarized (Light).tmTheme",
                "font_face": "Source Code Pro"
            }
        ]
    }
    


# Install 

### Easy Way

[Install via Package Control](http://wbond.net/sublime_packages/package_control)

### Hard Way

* Change to Sublime Text packages folder:

    * OS X `~/Library/Application Support/Sublime Text 2/Packages/User`
    * Windows `%APPDATA%\Sublime Text 2\Packages\User`
    * Linux `~/.config/sublime-text-2/Packages/User`

* Run the command:

    `git://github.com/chrislongo/QuickThemes.git`

* Set up your favorite themes to cycle through (see Info section above).
