# SMARTER Preference Elicitation Analysis Tool

Tool for analysing preferences elicited using the SMARTER methodology introduced by [Edwards and Barron](https://doi.org/10.1006/obhd.1994.1087) (1994).

## Getting Started

This tool provides a simple dashboard analyse results obtained from a survey utilising the SMARTER multi-attribute decision making methodology. It supports both nominal and numerical attributes, as well as a range of weight ranking methods (ROC, RS, RR, and some ROD). Resulting data from surveys has to be processed in a certain way in order to work with this tool, a CSV template is provided for that purpose.

### Prerequisites

* Python 3
* [Plotly Dash](https://dash.plotly.com/)
* Pandas
<!-- * [Pandas](https://pandas.pydata.org/) -->

<!-- ### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).  -->

## Usage

### Preparing data

When starting the program, it will try to load `input_data.csv` and `input_data_labels.json` files from the root directory to generate the analysis. If none are provided it will return default exmaple data.

These two files contain the actual survey output data and additional labelling for the analysis respectively. The latter of which might not always be required, depending on the source.

Currently implemented data sources are:

* Sawtooth Software Lighthouse Studio

For each of these sources, an example `input_data.csv` and `input_data_labels.json` are provided in the `example_datasets` folder. Additional requirements for each data source will also be specified there.

### Running app

Run app with:

```
$ python3 app.py
```

And visit [localhost:8050](http://localhost:8081/) in the browser.

<!-- ## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. -->

<!-- ## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details -->

<!-- ## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc -->
