# :microbe: covid-visuals

Development on covid-visuals has ended for the time being. This repository is archived and read-only.


[![Netlify Status](https://api.netlify.com/api/v1/badges/273356b5-3005-49de-b5e1-2f9f69a6cd07/deploy-status)](https://app.netlify.com/sites/covid-visuals/deploys)

[covid-visuals](https://covid-visuals.netlify.app/) is a website documenting the spread of COVID-19 and its impacts on the United States through custom visuals and a timeline of major events.

![covid-visuals front page](docs/content/images/cv_screen.png)

## Table of Contents

- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Technologies Used
- Python 3.8
- [Plotly](https://plotly.com/python/)
- JQuery 3.3.1
- [Fomantic-UI](https://fomantic-ui.com/)
- [marked.js](https://marked.js.org/)
- [AOS - Animate on Scroll Library](https://michalsnik.github.io/aos/)
- HTML / CSS / JS

## Setup
```
$ git clone https://github.com/vskbellala/covid-visuals.git
$ cd covid-visuals/
$ pip install -r requirements.txt
$ python3 update.py
$ cd docs/plots/
```
- Clone this repository and navigate to the root directory.
- Run `pip install -r requirements.txt` to install dependencies.
- Run `python3 update.py` to update plots.
- Navigate to `docs/plots/` and open a plot's HTML file to view them in the browser!

## Screenshots
### Pages
![Demo page title, blurb, and menu header](docs/content/images/safety.png)
![Sidebar focused](docs/content/images/sidebar_zoom.png)
![Sidebar pushing the page to reveal itself](docs/content/images/sidebar_push.png)
![Line plot for cases and deaths vs time](docs/content/images/case_plot.png)
### Timeline
![Sample timeline entry](docs/content/images/timeline_text.png)
![Plot in timeline, before launching](docs/content/images/timeline_before_play.png)
![Plot in timeline, after launching](docs/content/images/timeline_after_play.png)

## Contributing
We are not open to contributing at this time, but if you have any suggestions or comments, let us know by opening a [GitHub Issue](https://github.com/vskbellala/covid-visuals/issues).

## Acknowledgements
We greatly thank the following organizations for making this project possible. Their datasets have been invaluable to us.
- [The COVID Tracking Project](https://covidtracking.com/)
- [The New York Times](https://github.com/nytimes/covid-19-data)

## License
[GNU General Public License v3.0](https://github.com/vskbellala/covid-visuals/blob/master/LICENSE)
