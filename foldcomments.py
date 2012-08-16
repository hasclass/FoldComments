import sublime, sublime_plugin

class FoldFileComments(sublime_plugin.EventListener):
    def on_load(self, view):
        for region in view.find_by_selector('comment')
            view.fold(sublime.Region(region.a, region.b - 1))

class FoldCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.find_by_selector('comment')
            self.view.fold(sublime.Region(region.a, region.b - 1))


class UnfoldCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.find_by_selector('comment')
            self.view.unfold(sublime.Region(region.a, region.b - 1))
