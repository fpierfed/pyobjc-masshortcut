from PyObjCTools.TestSupport import *
from Cocoa import NSEventModifierFlagCommand
import MASShortcut

class TestMASShortcutMonitor (TestCase):
    def test_classes(self):
        MASShortcut.MASShortcutMonitor

    def test_methods(self):
        self.assertResultIsBOOL(MASShortcut.MASShortcutMonitor.registerShortcut_withAction_)
        self.assertResultIsBOOL(MASShortcut.MASShortcutMonitor.isShortcutRegistered_)

    def test_register_shortcut(self):
        def action():
            print('Shortcut pressed')

        shortcut = MASShortcut.MASShortcut.shortcutWithKeyCode_modifierFlags_(
            MASShortcut._constants.kVK_F1,
            NSEventModifierFlagCommand
        )
        mon = MASShortcut.MASShortcutMonitor.sharedMonitor()
        res = mon.registerShortcut_withAction_(shortcut, action)
        self.assertEqual(res, True)


if __name__ == "__main__":
    main()
