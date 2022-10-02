exports.helloWorld = async (req, res) => {


    const request = require('request');


    if ("text" in req.body.message && req.body.message.text === "/start") {
        const url = "https://api.telegram.org/bot<token>/sendMessage?chat_id=" + req.body.message.chat.id + "&text=Provide input";
        request.get(url);
    } else {
        const caption = req.body.message.caption;
        const photo = req.body.message.photo;
        const file_id = photo[photo.length - 1].file_id;
        const match = caption.match(/\b((?!=|\:|\:).)+(.)\b/g);
        const address = match[0];
        const title = match[1];
        const description = match[2];
        const url = "<metadata api url>?chat_id=" + req.body.message.chat.id + "&file_id=" + file_id + "&address=" + address + "&title=" + title + "&description=" + description + "";
        request.get(url);
    }
}
