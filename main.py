import controllers.Resume_Controller
from controllers.Resume_Controller import Resume_Controller

from dotenv import load_dotenv
import os

load_dotenv()
path = 'kataoka.pdf'
x = Resume_Controller(path)
x.run()