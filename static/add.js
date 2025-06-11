$(document).ready(function () {
    function add_show(new_show) {
        $.ajax({
            type: "POST",
            url: "/add_show",
            data: JSON.stringify(new_show),
            contentType: "application/json; charset=utf-8",  
            dataType: "json",  
            success: function(result) {
                console.log("Successfully added show.");

                // Update the page to display the success message dynamically
                let successMessage = `
                    <div class="alert alert-success">
                        '${new_show.title}' added successfully!
                        <a href="/view/${result.new_show_id}" class="see-link">See it here.</a>
                    </div>
                `;
                
                // Add success message above the form
                $("#add-form").before(successMessage);

                // Clear form fields after submission
                $("#add-form")[0].reset();
                $("#title").focus();
            },
            error: function(xhr, status, error) {
                console.log("Error saving show:", error);
                console.log("Response Text:", xhr.responseText);
            }
        });
    }

    $("#submit-btn").on("click", function (event) {
        event.preventDefault();

        let title = $("#title").val().trim();
        let image = $("#image").val().trim();
        let summary = $("#summary").val().trim();
        let genres = $("#genres").val().trim();
        let avg_ticket_price = $("#avg_ticket_price").val().trim();
        let avg_capacity = $("#avg_capacity").val().trim();
        let critics_score = $("#critics_score").val().trim();
        let weekly_grosses = $("#weekly_grosses").val().trim();
        let hasError = false;

        $(".error-message").remove();
        $("input").removeClass("input-error");

        if (title === "") {
            $("#title").addClass("input-error")
                .after('<span class="error-message text-danger">Title required</span>');
            hasError = true;
        }
        if (image === "") {
            $("#image").addClass("input-error")
                .after('<span class="error-message text-danger">Image URL required</span>');
            hasError = true;
        }
        if (summary === "") {
            $("#summary").addClass("input-error")
                .after('<span class="error-message text-danger">Summary required</span>');
            hasError = true;
        }
        if (genres === "") {
            $("#genres").addClass("input-error")
                .after('<span class="error-message text-danger">Genres required</span>');
            hasError = true;
        }

        let ticketPriceRegex = /^\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?$/;
        if (!ticketPriceRegex.test(avg_ticket_price)) {
            $("#avg_ticket_price").addClass("input-error")
                .after('<span class="error-message text-danger">Avg Ticket Price must be in format $100 or $100.50</span>');
            hasError = true;
        }

        let capacityRegex = /^\d{1,3}%$/;
        if (!capacityRegex.test(avg_capacity)) {
            $("#avg_capacity").addClass("input-error")
                .after('<span class="error-message text-danger">Avg Capacity must be in format 80%</span>');
            hasError = true;
        }

        let criticsScoreRegex = /^\d(\.\d{1,2})?\/10$/;
        if (!criticsScoreRegex.test(critics_score)) {
            $("#critics_score").addClass("input-error")
                .after('<span class="error-message text-danger">Critics Score must be in format 9.5/10</span>');
            hasError = true;
        }

        if (hasError) return;

        let new_show = {
            title: title,
            image: image,
            summary: summary,
            genres: genres,
            avg_ticket_price: avg_ticket_price,
            avg_capacity: avg_capacity,
            critics_score: critics_score,
            weekly_grosses: weekly_grosses
        };

        add_show(new_show);
    });
});
