# CDISC Library FAQ

This document consolidates commonly asked questions about accessing and using CDISC Library.

## What are the URLs for CDISC Library?

You can access the following sites via the links provided and add them to your bookmarks:

- **Data Standards Browser**: <https://library.cdisc.org/browser>
- **API Management Developer Portal**: <https://api.developer.library.cdisc.org>
- **Base URL for API**: <https://library.cdisc.org/api> (requires an API key from the API Management Developer Portal)

## Who can access CDISC Library?

CDISC Library is available to all employees of our Member Organizations as well as non-members.

## How do I access the CDISC Library data standards browser?

You can access the data standards browser with your existing CDISC Library credentials at <https://library.cdisc.org/browser>.

## Can I use my CDISC WIKI or CDISC website credentials to access the CDISC Library?

Your CDISC website credentials (cdiscID) can be used to access CDISC Library. If you do not have a cdiscID, please create one on the CDISC website.

## I have a CDISC Library account. Where can I find how-to articles to get started?

How-to articles can be found on the CDISC Library Service Desk Knowledge Base at <https://wiki.cdisc.org/display/LIBSUPRT/How-to+articles>.

## What is available in the CDISC Library?

A product catalog is posted on <https://www.cdisc.org/cdisc-library#cdisc__library__content>.

CDISC Library API customers can obtain a product catalog electronically by submitting `/mdr/products`.

## Does metadata in CDISC Library match those in the publications? Does it contain corrections?

CDISC requires metadata in CDISC Library to match what is originally published. Automated tools take the metadata from the specifications in the publications and put it into CDISC Library. The CDISC Library Release Notes describe where there are exceptions and/or limitations. CDISC is working to ensure that known issues in the published standards are addressed.

## Which part of a published standard is available in CDISC Library?

CDISC Library contains highly structured content such as domain specification tables from the SDTM, SENDIGs and SDTMIGs, metadata tables from CDASH and CDASHIG, data structure variables from ADaMIGs, and Controlled Terminology quarterly publications.

## Why does this query fail `/mdr/sdtm/1.6`?

CDISC Library uses dashes for version numbers. There is no `v` or `V`. `/mdr/sdtm/1-6` is the correct query.

## Why does this query fail `/mdr/sdtmig/3-2/classes/`?

The trailing forward slash is extra, which causes the error. `/mdr/sdtmig/3-2/classes` is the correct query.

## Why does this query fail `/mdr/SDTM/3-3`?

Path parameters are case sensitive. `/mdr/sdtm/3-3` is the correct query.

## What information can I use to help diagnose a failed query?

An HTTP status code is always returned after the server finishes processing a request. CDISC Library API generally follows HTTP/1.1 guidelines for status codes. For example, `200` indicates a successful request. When a query is not successful (status codes in the `4xx` or `5xx` series), a message will appear in the response body. For example, requesting a fictitious version of SDTMIG:

```http
HTTP/1.1 404
status: 404
Date: Wed, 29 May 2019 23:46:19 GMT
Content-Type: application/json
{
   "message": "Service resource error.",
   "detail": "Requested resource [http://library.cdisc.org/sdtmig-5-0/Product] does not exist."
}
```

For a list of supported HTTP status codes, visit <https://wiki.cdisc.org/display/LIBSUPRT/HTTP+Status+Codes>.

## Are there additional technical resources available?

Release Notes are available at <https://wiki.cdisc.org/display/LIBSUPRT/Release+Notes>. Additionally, CDISC continues to expand the knowledge base in the CDISC WIKI at <https://wiki.cdisc.org/display/LIBSUPRT/How-to+articles>.

## Is there documentation for CDISC Library API?

Yes. Visit the API Documentation on the CDISC website at <https://api.developer.library.cdisc.org/api-details>.

