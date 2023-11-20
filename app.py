from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    # You can customize the information to be displayed on the landing page
    company_name = "Your Company Heho"
    tagline = "Building a Better Future"
    about_us = "Welcome to {}! We are dedicated to {}. Explore our website to learn more.".format(company_name, tagline)
    
    return render_template('landing_page.html', company_name=company_name, tagline=tagline, about_us=about_us)

if __name__ == '__main__':
    app.run(debug=True)

# This is a change to the code
#hello Rzichard

