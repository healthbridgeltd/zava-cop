const { setWorldConstructor } = require("cucumber")
const { expect } = require("chai")
const puppeteer = require("puppeteer")

const accountLogin = "https://www.zavamed.com/de/account/#/login"

const email = '.qa-login-email'
const password = '.qa-login-password'

class LoginPage {
  constructor() {
    this.login = ""
  }

  async openPage(page) {
    this.browser = await puppeteer.launch()
    this.page = await this.browser.newPage()
    if (page === 'account login') {
      await this.page.goto(accountLogin)
    }
  }

  async fillPassword() {
    await this.page.waitForSelector(password)
    this.elePassword = await this.page.$(password)
    await this.elePassword.type('Katana,5')
  }

  async fillEmail() {
    await this.page.waitForSelector(email)
    this.eleEmail = await this.page.$(email)
    await this.eleEmail.type('automation_preview@zavamed.com')
  }

  async clickLogin() {
    this.eleEmail = await this.page.$('.qa-login-button')
    await this.eleEmail.click()
  }

  async waitForDashboard() {
    await this.page.waitForSelector('.sidebar-logout')
  }

  async closePage() {
    await this.browser.close()
  }
}

setWorldConstructor(LoginPage)