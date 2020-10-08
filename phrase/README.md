# Preparation

## Install Phrase command

For Mac users, it's easy to install with homebrew!
```
$ brew tap phrase/brewed
$ brew install phrase
```

For Linux or Windows users, please have a look the document: https://help.phrase.com/help/installation-1

Once you installed the command line, please run `phrase info` and you'll see

```
$ phrase info
Phrase client version:            2.0.13
Phrase client revision:           72a3b80ea91885b998de44a0199e353b419b9c69
Phrase library revision:          v1.0.10/go.mod
Last change at:                   Mon Aug 3 09:34:49 2020 +0000
Go version:                       go1.14.6
```

## npm install

We will use https://github.com/mashpie/i18n-node for integrate with Phrase, just execute commands below

```
$ npm install
$ node script.js en
phrase.hello
```

# Zava COP hands-on

![COP](/phrase/img/ss1.png)

### 1. Update .phrase.yml

- All the phrase project has a file called `.phrase.yml`, which specify the access token, project name, and where to store the files.
- Kohei will send `project_id` and `access_token` to all of you
  - Update `project_id: xxxxxxxxxxxxxxxxxxxx` to the real project id which is associated to 
  - Update `access_token: yyyyyyyyyyyyyyyyyyy` to the real access token (it will be disabled after the session)
- Run `phrase pull` and check if you can see `en.json` and `de.json` under `./locales` folder
- Execute a node command to see the result with translated
  - node index.js en
  - node index.js de

### 2. Fetch the updated data

- The second line is just showing `?`
- After the project was updated, run `phrase pull` to fetch the latest change on the Phrase project

### 3. Placeholders

- You can also use the place holder, currently, the third line shows `I am {{ name }}`
- Update the third one to `i18n.__('phrase.introduce', 'YOUR NAME')`
  - The format is supported by the library https://github.com/mashpie/i18n-node#i18n__
  - Phrase supports different formats of placeholders (e.g. Rails, Larabel etc) https://help.phrase.com/help/working-with-placeholders

### 4. Pluralization

- The translation files can also handle pluralization with `__n` function
- Change the fourth line to `i18n.__n('phrase.apple', 1)` to see singular, and change the number to `2` to see the plural form
- Ranged interval support: https://github.com/mashpie/i18n-node#ranged-interval-support

## Extra: Fetch different type of files
 - Change `file_format: simple_json` to fetch the file in different format (you'll also need to change the file name)
 - All the lists are https://help.phrase.com/help/supported-platforms-and-formats
   - Examples:
     - php_array (.php file for Kirby or other PHP projects)
     - gettext (.po file for Marc02)
     - go_i18n (.json file)
     - xml (.xml)
     - strings (.strings file for iOS)
