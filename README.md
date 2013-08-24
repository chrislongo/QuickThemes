# Info

QuickThemes allows you to easily cycle through any combination of Sublime Text 2 preferences. The obvious use is for changing color schemes, themes, and fonts simultaneously, but any of the ST2 preferences are available.

# Usage

Super+Alt+0: Cycle up  
Super+Alt+9: Cycle down

Alternatively, you can switch themes via Super+Shift+P and fuzzy search, e.g. "Super+Shift+P qtn" for next theme, "Super+Shift+P qtp" for previous theme.

# Configuration

Best to configure it to match your environments in:

`Preferences -> Package Settings -> QuickThemes -> Settings - User`

Any preference you want to change must be included in the "quick_theme_defaults"  section. Any preference not explicitly changed in a theme group will use the default. In the example below, the first group (#0) makes no changes; it simply makes the defaults available. The second group (#1) does not include a "font_size" preference, so it will use the default font_size of 12.

### Example

Two modes to harmonize with ambient light:

    {
        "quick_themes_selection": 0,
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
    `git clone https://github.com/chrislongo/QuickThemes.git`

* Set up your favorite themes to cycle through (see Info section above).
