/**
 * Vercel Speed Insights integration for Matter documentation
 * 
 * This script initializes Vercel Speed Insights for the Sphinx-based
 * Matter documentation site. It loads the analytics library and tracks
 * page performance metrics.
 * 
 * Installation:
 * 1. Enable Speed Insights in your Vercel project dashboard
 * 2. Deploy the site to Vercel
 * 3. Speed Insights data will appear in the Vercel dashboard after users visit
 * 
 * For more information, see: https://vercel.com/docs/speed-insights
 */

(function() {
  // Load the Vercel Speed Insights script
  window.si = window.si || function () {
    (window.siq = window.siq || []).push(arguments);
  };
  
  var script = document.createElement('script');
  script.defer = true;
  script.src = '/_vercel/speed-insights/script.js';
  
  // Append to head
  document.head.appendChild(script);
})();
