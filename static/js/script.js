document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("contactForm").addEventListener("submit", async function (e) {

        e.preventDefault();

        const formData = new FormData(this);

        // Show loading popup
        Swal.fire({
            title: "Sending Request...",
            text: "Please wait while we submit your request.",
            allowOutsideClick: false,
            allowEscapeKey: false,
            didOpen: () => {
                Swal.showLoading();
            }
        });

        try {

            const response = await fetch("/contact", {
                method: "POST",
                body: formData
            });

            // Close loading popup
            Swal.close();

            if (response.ok) {

                await Swal.fire({
                    icon: "success",
                    title: "Request Sent!",
                    text: "Your request has been sent successfully to SmartBot Automation. Our team will contact you soon.",
                    confirmButtonText: "OK"
                });

                // Clear form
                document.getElementById("contactForm").reset();

                // Go back to top of the page
                window.location.href = "/";

            } else {

                Swal.fire({
                    icon: "error",
                    title: "Submission Failed",
                    text: "Unable to send your request. Please try again."
                });

            }

        } catch (error) {

            Swal.close();

            Swal.fire({
                icon: "error",
                title: "Network Error",
                text: "Please check your internet connection and try again."
            });

            console.error(error);
        }

    });

});