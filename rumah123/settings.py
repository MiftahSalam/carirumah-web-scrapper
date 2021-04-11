
# print(__name__)

__all__ = [
    "HOME_PAGE",
    "RECOMMEND_CSS", 
    "POPULAR_CSS", 
    "NEW_PROPERTY_DETAIL_CSS", 
    "NEW_PROPERTY_DETAIL_OPEN_DIALOG_CSS", 
    "NEW_PROPERTY_CSS_SELECTORS", 
    "NEW_PROPERTY_DETAIL_SELECTORS",
    "BY_LOCATION_CSS",
    "BY_LOCATION_CSS_MORE_BTN",
    "BY_LOCATION_CSS_LIST",
    "BY_LOCATION_CSS_DETAIL",
    "PROPERTY_BY_CSS_SELECTORS",
]

HOME_PAGE = 'https://www.rumah123.com'

RECOMMEND_CSS =  'div[class="ui-container"] div[class="flex flex-row flex-wrap ui-row flex-align-start flex-justify-start"] div[class="ui-home-page__featured-property__card"] div[class="adunitContainer"]'

POPULAR_CSS =  'div[class="ui-home-page__popular-listing__content__card"] div[class="ui-atomic-card box-shadow-r123 ui-organisms-card-r123-popular"] a'
NEW_PROPERTY_DETAIL_CSS = '#other-projects > div > div > div > div > div > div > div.ui-molecules-toggle__content.relative > div > div.ui-molecules-tab__bar.ui-molecules-tab__bar--end.ui-molecules-tab__bar--start > div > div > div.ui-molecules-tab__pane'
NEW_PROPERTY_DETAIL_OPEN_DIALOG_CSS = '#other-projects > div > div > div > div > div > div > div.ui-molecules-toggle__content.relative > div > div.ui-molecules-tab__content > div > div'

BY_LOCATION_CSS = 'div[class="flex flex-row flex-wrap ui-row flex-align-start flex-justify-start"] div[class="r123-o-footer-r123__column relative ui-col-12"] section[class="flex flex-align-start flex-column ui-organism-footer-r123"] section[class="ui-organism-footer-r123__upper-section"] div[class="ui-container"] div[class="flex flex-row flex-wrap ui-row flex-align-start flex-justify-start"] div[class="relative ui-col-12"] div[class="ui-molecules-tab ui-molecules-tab-wrapper"] div[class="ui-molecules-tab__content"] div[class="ui-molecules-tabs__content"] div[class="block relative ui-molecules-toggle ui-molecules-toggle--expand"] div[class="ui-molecules-toggle__content relative"] div a[class="ui-atomic-link ui-organism-footer-r123__upper-section__active-content"]'
BY_LOCATION_CSS_MORE_BTN = 'div[class="flex flex-row flex-wrap ui-row flex-align-start flex-justify-start"] div[class="r123-o-footer-r123__column relative ui-col-12"] section[class="flex flex-align-start flex-column ui-organism-footer-r123"] section[class="ui-organism-footer-r123__upper-section"] div[class="ui-container"] div[class="flex flex-row flex-wrap ui-row flex-align-start flex-justify-start"] div[class="relative ui-col-12"] div[class="ui-molecules-tab ui-molecules-tab-wrapper"] div[class="ui-molecules-tab__content"] div[class="ui-molecules-tabs__content"] div[class="block relative ui-molecules-toggle"] div[class="relative ui-molecules-toggle__selector ui-molecules-toggle__selector--bottom"] span'
BY_LOCATION_CSS_DETAIL = '#card-carousel'
BY_LOCATION_CSS_LIST = 'div[class="sc-pFZIQ gbgfMs"] div[class="sc-hKgILt gTLZXx"] div[class="ui-container flex flex-justify-between flex-align-start relative"] div[class="left-container-wrapper flex flex-row flex-wrap ui-row flex-align-start flex-justify-start"] div div[class="sc-eCssSg hmocIu"]'

NEW_PROPERTY_CSS_SELECTORS = {
    "property_name": 'h1[class*="ui-organism-property-summary__name"]',
    "address": 'h2[class*="ui-organism-property-summary__address"]',
    "property_type": 'p[class*="ui-molecules-tab-list-r123-detail__attribute--value"]',
    "description": 'div[class="ui-organisms-listing-description-r123__detail"] div[class="block relative ui-molecules-toggle ui-molecules-toggle--gradient"] div[class="ui-molecules-toggle__content relative"] p[class="ui-atomic-text ui-atomic-text--styling-default ui-atomic-text--typeface-primary"]',
    "release_date": 'div[class="ui-organism-property-summary__attribute-info"] div[class="ui-organism-property-summary__attribute__value"]',
    "developer": {
        'developer_name': 'p[class*="ui-organism-property-summary__developer"] a[class*="ui-molecules-hollow-link"] span[class*="ui-atomic-link--children"]',
        'developer_contact': 'div[class="truncate ui-atomic-ellipsis"]'
    }, 
    "agent": {
        'agent_name': '',
        'agent_contact': '',
    }, 
    "publish_date": '',
    "catalog_link": '',
    "facility": '',
    "status": '',
    "certificate": '',	
    "geo_location": '',
}

NEW_PROPERTY_DETAIL_SELECTORS = {
    "name": 'h5[class*="ui-organism-project-unit-r123__dialog-title"]',
    "price": '#other-projects > div > div > div > div > div.ui-organism-project-unit-r123__dialog.ui-organism-project-unit-r123__dialog--first-image.ui-atomic-dialog.ui-atomic-dialog--type-popup.ui-atomic-dialog__show.fade-enter-done > div.ui-atomic-dialog__content.absolute.no-m > div.ui-organism-project-unit-r123__dialog-info-attribute > p',
    "LT": '#other-projects > div > div > div > div > div.ui-organism-project-unit-r123__dialog.ui-organism-project-unit-r123__dialog--first-image.ui-atomic-dialog.ui-atomic-dialog--type-popup.ui-atomic-dialog__show.fade-enter-done > div.ui-atomic-dialog__content.absolute.no-m > div.ui-organism-project-unit-r123__dialog-info-attribute > div.flex.ui-molecules-list__divider-none--horizontal.flex-align-center.flex-row.flex-wrap.relative.ui-molecules-list.ui-organism-project-unit-r123__dialog-land-size > div:nth-child(1) > a > span',
    "LB": '#other-projects > div > div > div > div > div.ui-organism-project-unit-r123__dialog.ui-organism-project-unit-r123__dialog--first-image.ui-atomic-dialog.ui-atomic-dialog--type-popup.ui-atomic-dialog__show.fade-enter-done > div.ui-atomic-dialog__content.absolute.no-m > div.ui-organism-project-unit-r123__dialog-info-attribute > div.flex.ui-molecules-list__divider-none--horizontal.flex-align-center.flex-row.flex-wrap.relative.ui-molecules-list.ui-organism-project-unit-r123__dialog-land-size > div:nth-child(2) > a > span',
    "images__attr__src": 'div[class*="ui-organism-project-unit-r123__dialog-carousel"] div[class="ui-molecules-carousel__slider relative"] div[class="ui-molecules-carousel__item relative"] img',
    'el_action_close_detail__click': '#other-projects > div > div > div > div > div.ui-organism-project-unit-r123__dialog.ui-organism-project-unit-r123__dialog--first-image.ui-atomic-dialog.ui-atomic-dialog--type-popup.ui-atomic-dialog__show.fade-enter-done > div.ui-atomic-dialog__content.absolute.no-m > i', #close detail
}

PROPERTY_BY_CSS_SELECTORS = {
    "property_name": 'div.ui-organisms-listing-description-r123__detail > h2',
    "address": 'div.flex.r123-o-listing-summary__detail--address > h1',
    "developer": {
        'developer_name': '',
        'developer_contact': ''
    }, 
    "agent": {
        'agent_name': 'div.ui-organism-listing-inquiry-r123__contact-form-title h2 > b > a',
        'agent_contact': 'div.ui-organism-listing-inquiry-r123__container-wrapper > div > a > span.ui-atomic-button--children > div',
    }, 
    "price": 'div.r123-o-listing-summary.relative > div:nth-child(2) > div:nth-child(1) > span',
    "LT": 'div.r123-o-listing-summary__detail--area-info > div > div > div > div:nth-child(2) > a > span',
    "LB": 'div.r123-o-listing-summary__detail--area-info > div > div > div > div:nth-child(1) > a > span',
    "status": 'div.r123-o-listing-summary.relative > div:nth-child(1) > p',
    'el_action_open_detail__click': 'div.relative.ui-molecules-list__item.flex.flex-align-center.flex-justify-center', #open detail
    "images__attr__src": 'li[class*="relative ui-organism-gallery__thumbnail-item"] img',
    'el_action_close_detail__click': 'div.ui-atomic-dialog__content.absolute.no-m > i', #close detail
    "release_date": '',
    "catalog_link": '',
    "facility": '',
    "geo_location": '',
    "name": '',
}