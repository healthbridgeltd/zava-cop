const { Given, When, Then, After } = require('cucumber')

After(async function () {
  return await this.closePage()
});

Given('a {string} is on the {string} page', async function (user, page) {
  return await this.openPage(page)
})

When('the {string} fills out their login details', async function (user) {
  await this.fillEmail()
  await this.fillPassword()
})

When('clicks login', async function () {
  return await this.clickLogin()
})


Then('the {string} is taken to the {string} steps', async function (user, page) {
  return await this.waitForDashboard()
})