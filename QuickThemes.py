import sublime
import sublime_plugin
import re


class QuickThemesCommand(sublime_plugin.WindowCommand):
    def run(self, action):

        base_settings = sublime.load_settings("Base File.sublime-settings")
        settings = sublime.load_settings(__name__ + '.sublime-settings')

        current_theme = base_settings.get("color_scheme")
        themes = settings.get("quick_themes")

        if current_theme in themes:
            index = themes.index(current_theme)

            if action == "inc":
                index += 1
                if index > len(themes) - 1:
                    index = 0
            else:
                index -= 1
                if index < 0:
                    index = len(themes) - 1
        else:
            index = 0

        base_settings.set("color_scheme", themes[index])
        sublime.save_settings("Base File.sublime-settings")

        match = re.search("([^/]+).tmTheme|.sublime-theme$", themes[index])

        if match:
            theme_name = match.group(1)
            sublime.status_message(theme_name)
