function sleep(milliseconds) {
    var start = new Date().getTime();
    while (true) {
        if ((new Date().getTime() - start) > milliseconds) {
            break;
        }
    }
}

function deleteMessages() {

    const authorId = "ENTER_HERE_UR_ID";
    const channelId = "ENTER_HERE_CHANNEL_ID";
    const deleteAfter = "search?author_id=" + authorId + "&min_id=000000000000000000";
    const baseURL = "https://discordapp.com/api/v6/channels/" + channelId + "/messages/";
    const authToken = document.body.appendChild(document.createElement("iframe"))
        .contentWindow.localStorage.token.replace(/"/g, "");

    const headers = {
        "Authorization": authToken
    };

    fetch(baseURL + deleteAfter, {
            headers
        })
        .then(resp => resp.json())
        .then(result => {
            console.log("There are " + result.total_results + " messages left to delete.");
            if (result.total_results == 0) {
                alert("All the messages got deleted. \nPlease refresh the page before pressing 'OK'.");
            }
            result.messages.forEach(function(element) {
                element.forEach(function(message) {
                    if (message.author.id == authorId && message.hit == true) {
                        console.log("Deleting message with Id #" + message.id);
                        console.log(baseURL + message.id);
                        fetch(baseURL + message.id, {
                            headers,
                            method: "DELETE"
                        });
                    }
                });
                sleep(500);
            });
        })
        .then(() => deleteMessages());
}

deleteMessages();
