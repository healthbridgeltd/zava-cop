import i18n from 'i18n'
import path from 'path'

/**
 * To execute the script
 * $ node script.js en --> Start with 'en' locale
 * $ node script.js de --> Start with 'de' locale
 */

const args = process.argv.slice(2);
i18n.configure({
  locales: ['en', 'de'],
  defaultLocale: 'en',
  directory: path.join('./', 'locales'),
  api: {
    '__': 'translate',
    '__n': 'translateN'
  },
})
i18n.setLocale(args[0])

console.log(i18n.__('phrase.hello'))
console.log(i18n.__('phrase.greeting'))
// console.log() // For '3. Placeholders'
// console.log() // For '4. Pluralization'
