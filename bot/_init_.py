

# Import the main function from the bot module
from .bot import main

# You can also import any other functions or classes you want to be directly accessible
from .commands import start, help

from bot import main, start, help

# Now you can call main() directly
if __name__ == "_main_":
    main()
    # bot/_init_.py