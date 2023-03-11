# LinkedIn Impression Booster

This project is a simple script that takes links of LinkedIn posts as input and uses Selenium to open the links, wait for a random amount of time between `seconds` and `seconds+5`, and refresh the page. This is done to increase the impression count for the post. However, it's important to note that engagement is more important than impression, so this project is not intended to be used to artificially boost engagement.

## **Prerequisites**

To run this script, you will need the following installed on your system:

- Python 3.x
- Selenium
- ChromeDriver (or another compatible web driver)

## **Installation**

1. Clone this repository to your local machine using git clone `https://github.com/amyrmahdy/linkedin-impression-booster.git`

2. Install the required dependencies using `pip install -r requirements.txt`

## **Usage**

1. Add the links of the LinkedIn posts you want to boost impressions for to a file named `input.txt` (one link per line).

2. Run the script using `python main.py <views> <seconds>`, where `<views>` is the number of times the page should be refreshed and `<seconds>` is the base number of seconds to wait before refreshing. If no arguments are provided, default values of `1000` for views and `5` for seconds will be used.

3. Watch as the script opens each link, waits for a random amount of time, and refreshes the page to boost the impression count.

## **Notes**

- This project is for educational purposes only and should not be used to artificially inflate engagement on LinkedIn.

- Be mindful of LinkedIn's terms of service and community guidelines when using this project.

- The script is currently set up to use `ChromeDriver`. If you want to use a different web driver, update the `executable_path` in `playing()` accordingly.

## **License**

This project is licensed under the MIT License

## **Contributing**

Contributions are welcome! If you find a bug or want to suggest an improvement, please create an issue or submit a pull request.


<br >
<br >

**Author: amyrmahdy**

**Date: 8 March 2023**





