# Vercel Web Analytics Integration

This documentation site is configured with Vercel Web Analytics to track page
views and user interactions.

## How It Works

The analytics integration is implemented using a custom JavaScript file that
loads the Vercel Analytics script when the documentation is deployed on Vercel.

### Implementation Details

1. **JavaScript Integration**: A custom analytics script is located at
   `docs/_static/js/vercel-analytics.js` that initializes the Vercel Analytics
   tracking code.

2. **Sphinx Configuration**: The analytics script is automatically included in
   all documentation pages through the `html_js_files` configuration in
   `docs/conf.py`.

3. **Graceful Degradation**: The analytics script gracefully handles cases
   where it's not deployed on Vercel (e.g., local development) by catching and
   logging any script loading errors.

## Enabling Analytics on Vercel

To enable Web Analytics for the deployed documentation:

1. **Deploy to Vercel**: Ensure the documentation site is deployed to Vercel
   (either the main `connectedhomeip-doc` repository or a custom deployment).

2. **Enable Analytics in Dashboard**:
    - Go to your project in the Vercel dashboard
    - Navigate to the "Analytics" tab
    - Enable "Web Analytics"
    - Deploy your site (or wait for the next automatic deployment)

3. **Verification**: After deployment, you can verify analytics are working by:
    - Opening the deployed site in a browser
    - Opening the browser's Developer Tools (F12)
    - Checking the Network tab for requests to `/_vercel/insights/`
    - Viewing analytics data in the Vercel dashboard (data appears after the
      first visitors)

## Local Development

During local development (using `make html` to build the documentation), the
analytics script will attempt to load but will fail gracefully with a console
message. This is expected behavior and does not affect the documentation build
or local viewing experience.

## Files Modified

-   `docs/conf.py`: Added `html_js_files` configuration to include the
    analytics script
-   `docs/_static/js/vercel-analytics.js`: Custom JavaScript integration for
    Vercel Analytics

## Additional Resources

-   [Vercel Web Analytics Documentation](https://vercel.com/docs/analytics)
-   [Vercel Analytics Quickstart](https://vercel.com/docs/analytics/quickstart)
