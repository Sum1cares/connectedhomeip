# Vercel Speed Insights Integration

This documentation site is configured with Vercel Speed Insights to monitor and
track real user performance metrics.

## What is Speed Insights?

Vercel Speed Insights provides real-time performance monitoring that captures
actual user experience metrics including:

-   **First Contentful Paint (FCP)**: Time until first content is rendered
-   **Largest Contentful Paint (LCP)**: Time until largest content is rendered
-   **Cumulative Layout Shift (CLS)**: Visual stability metric
-   **First Input Delay (FID)**: Interactivity metric
-   **Time to First Byte (TTFB)**: Server response time

These metrics help identify performance bottlenecks and ensure the documentation
provides a fast, smooth experience for all users.

## How It Works

The Speed Insights integration is implemented using a custom JavaScript file
that loads the Vercel Speed Insights script when the documentation is deployed
on Vercel.

### Implementation Details

1. **JavaScript Integration**: A custom Speed Insights script is located at
   `docs/_static/js/vercel-speed-insights.js` that initializes the Vercel Speed
   Insights tracking code.

2. **Sphinx Configuration**: The Speed Insights script is automatically included
   in all documentation pages through the `html_js_files` configuration in
   `docs/conf.py`.

3. **Graceful Degradation**: The Speed Insights script gracefully handles cases
   where it's not deployed on Vercel (e.g., local development) by catching and
   logging any script loading errors.

## Enabling Speed Insights on Vercel

To enable Speed Insights for the deployed documentation:

1. **Deploy to Vercel**: Ensure the documentation site is deployed to Vercel
   (either the main `connectedhomeip-doc` repository or a custom deployment).

2. **Enable Speed Insights in Dashboard**:

    - Go to your project in the Vercel dashboard
    - Navigate to the "Speed Insights" tab
    - Click the "Enable" button
    - Deploy your site (or wait for the next automatic deployment)

3. **Verification**: After deployment, you can verify Speed Insights are working
   by:
    - Opening the deployed site in a browser
    - Opening the browser's Developer Tools (F12)
    - Checking the Network tab for requests to `/_vercel/speed-insights/`
    - Viewing performance data in the Vercel dashboard (data appears after
      visitors interact with the site)

## Local Development

During local development (using `make html` to build the documentation), the
Speed Insights script will attempt to load but will fail gracefully with a
console message. This is expected behavior and does not affect the documentation
build or local viewing experience.

## Performance Monitoring

Once enabled, Speed Insights provides:

-   **Real-time Performance Dashboard**: View current performance metrics
-   **Historical Trends**: Track performance changes over time
-   **Device and Network Breakdown**: See how performance varies by device type
    and connection speed
-   **Page-level Insights**: Identify which pages need optimization
-   **Core Web Vitals Tracking**: Monitor Google's key performance metrics

## Files Modified

-   `docs/conf.py`: Added `vercel-speed-insights.js` to `html_js_files`
    configuration
-   `docs/_static/js/vercel-speed-insights.js`: Custom JavaScript integration
    for Vercel Speed Insights

## Relationship with Web Analytics

This documentation site uses both:

-   **Vercel Web Analytics** (see [VERCEL_ANALYTICS.md](VERCEL_ANALYTICS.md)):
    Tracks page views and user behavior
-   **Vercel Speed Insights** (this document): Monitors performance metrics

Both integrations work independently and provide complementary insights into how
users interact with and experience the documentation.

## Additional Resources

-   [Vercel Speed Insights Documentation](https://vercel.com/docs/speed-insights)
-   [Vercel Speed Insights Quickstart](https://vercel.com/docs/speed-insights/quickstart)
-   [Web Vitals](https://web.dev/vitals/): Google's initiative for quality
    signals essential to great user experience
