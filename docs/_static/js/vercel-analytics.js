/**
 * Vercel Web Analytics Integration
 * This script injects Vercel Analytics tracking into the documentation site.
 */
(function () {
    // Initialize Vercel Analytics queue
    window.va =
        window.va ||
        function () {
            (window.vaq = window.vaq || []).push(arguments);
        };

    // The actual analytics script will be loaded from Vercel's CDN
    // when the site is deployed on Vercel with Analytics enabled
    var script = document.createElement("script");
    script.defer = true;
    script.src = "/_vercel/insights/script.js";

    // Only load if the script exists (i.e., when deployed on Vercel)
    script.onerror = function () {
        console.log(
            "Vercel Analytics not available - this is expected in local development",
        );
    };

    document.head.appendChild(script);
})();
