# Sample beaTlet for beaTunes 4.x
# More info at https://www.beatunes.com/en/beatlet-getting-started.html
from javax.swing import *
from com.tagtraum.core.app import *
from com.tagtraum.beatunes import MessageDialog
from com.tagtraum.beatunes.action import *
# Needed for Java array creation
from jarray import array

class DialogAction(BaseAction):

    def getId(self):
        return "Jython.DialogAction"

    def init(self):
        self.putValue(Action.NAME, "DialogAction")

    def getActionLocations(self):
        # Java array creation via array([], type)
        return array([AbsoluteActionLocation(BeaTunesUIRegion.TOOL_MENU,
            AbsoluteActionLocation.LAST)], ActionLocation)

    def actionPerformed(self, actionEvent):
        MessageDialog(
            self.getApplication().getMainWindow(),
            "DialogAction",
            JOptionPane.INFORMATION_MESSAGE,
            JOptionPane.DEFAULT_OPTION
        ).showDialog()

