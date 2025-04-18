$(document).ready(function() {
    // Fetch news from the backend
    $.get('/get_news', function(news) {
        let newsContainer = $('#news-container');
        news.forEach(function(article) {
            let card = `
                <div class="news-card">
                    <h2>${article.title}</h2>
                    <p>${article.summary}</p>
                    <a href="${article.link}" target="_blank">Read full article</a>
                </div>
            `;
            newsContainer.append(card);
        });
    });
});
