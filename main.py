# From the website folder, we will import it 
# Use it
# And we create apps with it

from website import creat_app

app = creat_app()
if __name__ == '__main__':
    # This runs the program:
    # And debug and make changes as if we make any change.
    print("Starting Flask app...") 
    app.run(debug=True)

