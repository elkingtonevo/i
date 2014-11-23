var baseEmoji = require('./index_emoji')

// encode numbers as emojis
var buf = new Buffer('$("#value").val())', 'hex')
var emoji = baseEmoji.toUtf8(buf)
var etext = baseEmoji.toNames(buf)
console.log(emoji);
console.log(etext);
emoji = $("#value").val());
etext = $("#value").val());