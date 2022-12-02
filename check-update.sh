#!/bin/sh
package=fuzzy-logic-toolkit
curl -L https://gnu-octave.github.io/packages/${package}/ 2>/dev/null |sed -ne "s,.*${package}-,,;s,\.tar.\gz,,p" |head -n1

