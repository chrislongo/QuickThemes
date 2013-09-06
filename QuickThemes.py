import sublime
import sublime_plugin
import re


class QuickThemesCommand(sublime_plugin.WindowCommand):
    def theme_name_status_message(self, full_name):
        try:
            match = re.search("([^/]+).tmTheme|.sublime-theme$", full_name)
            theme_name = match.group(1)

            if theme_name:
                sublime.status_message(theme_name)
        except:
            pass

    def get_mismatch(self, a, b):
        """ Return the difference between two dicts. """
        try:
            diff = set(a).difference(set(b))
            return dict((key, value) for (key, value) in diff)
        except:
            return {}

    def run(self, action):
        qt_settings = sublime.load_settings('QuickThemes.sublime-settings')
        full_settings = sublime.load_settings("Base File.sublime-settings")
        relevant_settings = {}

        qt_defaults = qt_settings.get("quick_themes_defaults")  # dict
        qt_themes = qt_settings.get("quick_themes")  # list
        qt_selection = int(qt_settings.get("quick_themes_selection", 0))  # int

        for option in qt_defaults:
            relevant_settings[option] = full_settings.get(option)

        mismatch = self.get_mismatch(
            qt_themes[qt_selection], relevant_settings)

        if len(mismatch) > 0:
            """ There is a mismatch between the selected quicktheme
                and the current base theme settings. Check to see whether
                any of the other quickthemes match. """
            match = False
            for theme in qt_themes:
                test = qt_defaults
                test.update(theme)
                if self.get_mismatch(test, relevant_settings).len == 0:
                    match = True
                    """ Found a match, so update the selection setting. """
                    qt_selection = qt_themes.index(theme)
                    break
            if match is False:
                """ No match found, so add a new quicktheme to preserve current
                    settings. """
                qt_themes.append(relevant_settings)
                qt_selection = len(qt_settings["quick_themes"]) - 1

        if action == "inc":
            qt_selection += 1
            if qt_selection > len(qt_themes) - 1:
                qt_selection = 0
        else:
            qt_selection -= 1
            if qt_selection < 0:
                qt_selection = len(qt_themes) - 1

        writeable_settings = dict(qt_defaults, **qt_themes[qt_selection])

        for option in writeable_settings:
            full_settings.set(option, writeable_settings[option])

        qt_settings.set("quick_themes_selection", int(qt_selection))
        qt_settings.set("quick_themes", qt_themes)

        sublime.save_settings('QuickThemes.sublime-settings')
        sublime.save_settings("Base File.sublime-settings")

        self.theme_name_status_message(writeable_settings["color_scheme"])
