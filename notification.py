import time
import os
from winotify import Notification, audio # type: ignore

script_dir = os.path.dirname(__file__)
icon_path = os.path.join(script_dir, "Image", "gettyimages-132071705-612x612.jpg")

if os.path.exists(icon_path):
    toast = Notification(app_id="GPCorporation",
                     title="Vous êtes invitez à répondre a un:",
                     msg="QUIZ ENGLISH !!",
                     duration="long",
                     icon=icon_path)
    toast.set_audio(audio.SMS, loop=False)
else:
    toast = Notification(app_id="GPCorporation",
                     title="L'image n'a pas été trouvée à ce chemin :",
                     msg="icon_path",
                     duration="long")
    toast.set_audio(audio.Mail, loop=False)



#toast.add_actions(label="", launch="") Pour lancer une actions
toast.show()