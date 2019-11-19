# Cosmetic Safety Scanner
Cosmetic use worldwide is growing rapidly, without much concern to what is truly safe for use. Using optical character recognition, this web app cross-references ingredient lists with hazardous chemical databases to find the potential health risks associated with the chemicals in a gien product.

## How it works
1. Go to https://cosmetic-safety-scanner.herokuapp.com
2. Upload a photo or use the webcam to take a photo of a cosmetic product's ingredient list.
3. Our tool will display a list of the potentially dangerous chemicals identified in the ingredient list.
4. Share your results or scan another product!

## Technical specs
This app runs on Flask and is coded in Python, with a user interface designed in HTML/CSS/JS. Chemical databases used are a combination of our personally compiled data and online resources.

## Disclaimer
Much of the research done on cosmetic ingredients is as yet inconclusive. The purpose of the app is simply to identify *potential* risks. As such, we will err on the side of safety and report potential risks whenever applicable. In addition, our databases are not complete, so even a product that the app reports as "safe" may contain hazardous chemicals. 

The ultimate goal of the web app is not to provide a complete solution to scanning cosmetic ingredients. It is simply to stimulate thought, to create more accountability in the cosmetic industry.
