# githubActions-OrderADominosPizza
Hey gang! Professor Feeser here. This repository lets you use GitHub actions, Firefox and Selenium to order a Dominos Pizza! In order to make this script work, you'll need to set the following GitHub secrets:

- `secrets.EMAIL` - Email address to attach to your order
- `secrets.PHONE` - Phone number to associate with your Dominos order
- `secrets.FIRST_NAME` - First name on your Dominos order
- `secrets.LAST_NAME` - Last name on your Dominos order
- `secrets.ZIPCODE` - Zipcode to find closest store in your area


## Structure
### /
  - **order.py** - This is the script that does the ordering. The order itself is paid for in cash, therefore, for security, the final "order" click is commented out. You need to uncomment this yourself to make the script work correctly.
  - **requirements.txt** - Python requirements to make the script function.

### /.github/workflows
  - **order.yml** - A GitHub workflow that uses Selenium to order the pizza.
  

## Video Demos
Videos demonstrating the code in this repository are available on the author's [YouTube Channel @CodeWithFeeser](https://www.youtube.com/@CodeWithFeeser):  

- [YouTube CodeWithFeeser - Learn GitHub Actions - Order a Dominos Pizza]()


If you found a video helpful, be sure to hit **like** and **subscribe** for weekly lessons from [YouTube Channel @CodeWithFeeser](https://www.youtube.com/@CodeWithFeeser)


## How to Use This Repository
This repository is a best practice repository I use for teaching structure and organization of Selenium and GitHub actions. If you have any suggestions, feel free to open an issue. If you haven't already, be sure to watch the videos I have posted on using the content found in this repository.


## Helpful Notes
- When the Workflow concludes, it creates an artifact of a screenshot taken of the last thing Selenium "saw" before concluding. This is valuable for confirming your pizza is on the way, or for troubleshooting.
- Selenium must be able to "see" an element, or it will fail to find that element. Increasing the resolution of the driver fixed lots of issues relating to being able to "find" elements when Selenium was transfered from my Desktop to a container runtime environment 


## Help & Training
Since 2010 I've been providing in person and online technical training solutions for large organizations and individuals. If you're looking for a training solution, reach out via my [contact portal at IRIS7](https://iris7.com/contact).
