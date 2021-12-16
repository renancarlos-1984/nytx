function book_detail() {
    books = document.getElementsByClassName("authorx");
    for (var i=0; i<books.length; i++) {
        books[i].addEventListener("click", function(ev) {
            ev.preventDefault();
            var url = this.getElementsByTagName("a")[0].href;
            get_book_data(url);            
        });
    }
}


function get_book_data(url) {
    fetch(url)
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        load_main_book(data);
    })
}

function load_main_book(data) {
    title = document.getElementById("main-title");
    title.innerText = titlecase(data["book"]["title"]);
    author = document.getElementById("main-author");
    author.innerText = "by " + data["book"]["author"];
    img = document.getElementById("main-cover");
    img.src = data["book"]["book_image"];
    desc = document.getElementById("main-desc");
    desc.innerText = data["book"]["description"];
    rank = document.getElementById("main-rank");
    rank_text = "Rank: " + data["book"]["rank"] + "\n";
    rank_text += "Weeks on List: " + data["book"]["rank"]
    rank.innerText = rank_text
}

function titlecase(str) {
    str = str.toLowerCase().split(" ");
    for (var i = 0; i < str.length; i++) {
        str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1);
    }
    return str.join(" ")
}

book_detail();



