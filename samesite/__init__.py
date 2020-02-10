# -*- coding: utf-8 -*-
import re


__all__ = [
    'should_send_samesite_none',
    'is_samesite_none_incompatible',
]


def should_send_samesite_none(useragent: str):
    return not is_samesite_none_incompatible(useragent)


def is_samesite_none_incompatible(useragent: str):
    return has_webkit_samesite_bug(useragent) or drops_unrecognized_samesite_cookies(useragent)


def has_webkit_samesite_bug(useragent: str):
    return (
        is_ios_version(12, useragent) or
        (
            is_macosx_version(10, 14, useragent) and
            (is_safari(useragent) or is_mac_embedded_browser(useragent))
        )
    )


def drops_unrecognized_samesite_cookies(useragent: str):
    if is_uc_browser(useragent):
        return not is_uc_browser_version_at_least(12, 13, 2, useragent)
    return (
        is_chromium_based(useragent) and
        is_chromium_version_at_least(51, useragent) and
        not is_chromium_version_at_least(67, useragent)
    )


def is_ios_version(major: int, useragent: str):
    match = re.search(r'\(iP.+; CPU .*OS (\d+)[_\d]*.*\) AppleWebKit/', useragent)
    return match and int(match.group(1)) == major


def is_macosx_version(major: int, minor: int, useragent: str):
    match = re.search(r'\(Macintosh;.*Mac OS X (\d+)_(\d+)[_\d]*.*\) AppleWebKit/', useragent)
    return match and (int(match.group(1)) == major) and (int(match.group(2)) == minor)


def is_safari(useragent: str):
    return re.search(r'Version/.* Safari/', useragent) and not is_chromium_based(useragent)


def is_mac_embedded_browser(useragent: str):
    return bool(
        re.search(
            r'^Mozilla/[.\d]+ \(Macintosh;.*Mac OS X [_\d]+\) AppleWebKit/[.\d]+ \(KHTML, like Gecko\)$',
            useragent
        )
    )


def is_chromium_based(useragent: str):
    return bool(re.search(r'Chrom(e|ium)', useragent))


def is_chromium_version_at_least(major: int, useragent: str):
    match = re.search(r'Chrom[^ /]+/(\d+)[.\d]* ', useragent)
    return match and int(match.group(1)) >= major


def is_uc_browser(useragent: str):
    return "UCBrowser/" in useragent


def is_uc_browser_version_at_least(major: int, minor: int, build: int, useragent: str):
    match = re.search(r'UCBrowser/(\d+)\.(\d+)\.(\d+)[.\d]* ', useragent)
    if not match:
        return False
    major_version = int(match.group(1))
    minor_version = int(match.group(2))
    build_version = int(match.group(3))
    if major_version != major:
        return major_version > major
    if minor_version != minor:
        return minor_version > minor
    return build_version >= build
