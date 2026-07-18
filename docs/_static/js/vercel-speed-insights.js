/**
 * Vercel Speed Insights Integration
 * This script injects Vercel Speed Insights tracking into the documentation site.
 */
(function () {
    // Create the Speed Insights script element
    var script = document.createElement("script");
    script.defer = true;
    script.src = "/_vercel/speed-insights/script.js";

    // Only load if the script exists (i.e., when deployed on Vercel)
    script.onerror = function () {
        console.log(
            "Vercel Speed Insights not available - this is expected in local development",
        );
    };

    document.head.appendChild(script);
})();
