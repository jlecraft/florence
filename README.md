# Florence homes shortlist

This folder contains a static page comparing eight homes in Florence, Oregon. The cards and comparison table follow the preference order below. Clicking a photo opens the property listing; clicking an address opens Google Maps. The home name in the comparison table jumps to its card.

## Continue development

Edit the `homes` list and card/table markup in `build.py`, and edit presentation in `style.css`. Then run:

```sh
python3 build.py
./copy-to-videos.sh
```

The build writes `index.html`, a self-contained `Florence-Homes.html`, and `florence-homes.zip`. The copy script puts `index.html`, `style.css`, and `assets/` in `~/Videos/florence/`; run it **after** building when that copy should be updated. It does not copy the self-contained page or ZIP. The site has no JavaScript, package manager, server dependency, or automated test suite. For a local preview, run `python3 -m http.server 8000` and open `http://localhost:8000/`.

`AGENTS.md` has contributor conventions. `house_list.txt` preserves the original links and notes; its order is historical, not the current page order. Generated HTML should be changed through `build.py`, since rebuilding overwrites direct edits.

## Current preference order

| Rank | Address | MLS | Photo |
| --- | --- | --- | --- |
| 1 | 83362 Parkway Dr | 745319223 | `assets/01.jpg` |
| 2 | 5590 S Shore Dr | 152806514 | `assets/02.jpg` |
| 3 | 89555 Shore Crest Dr | 270810465 | `assets/03.jpg` |
| 4 | 4792 Rhododendron Loop | 415050331 | `assets/04.jpg` |
| 5 | 240 11th St | 145264700 | `assets/05.jpg` |
| 6 | 5045 N Loftus Rd | 183278526 | `assets/06.jpg` |
| 7 | 85405 Armstrong Way | 385016516 | `assets/07.jpg` |
| 8 | 5665 Peninsula Rd | 358008118 | `assets/08.jpg` |

If the order changes, reorder both the `homes` entries and their numbered photos. The first card receives the “Our first choice” label automatically. Keep personal notes consistent with the new order.

## Listing data and checks

The displayed taxes are **2025 property taxes**, rounded to whole dollars; they are not a forecast. Listing facts were checked September 26, 2026 and may change. Most photo links use the Zillow URL constructed in `build.py`. Two homes have address-specific listing overrides: [4792 Rhododendron Loop](https://www.lanecountyhomes.net/property-search/detail/53/415050331/4792-rhododendron-loop-florence-or-97439/) uses MLS data because Zillow incorrectly labels it single-family and shows older taxes; it is manufactured, with public water and standard septic. [85405 Armstrong Way](https://keithmccuerealty.com/Lane/OR/85405-armstrong-way-97439/385016516) uses the current MLS listing; its 1.38-acre listing includes an additional lot, while Zillow's older record lists 0.69 acres. “Sale pending” for Peninsula Road is a personal note and should be verified before treating it as current status.

After editing, check that there are eight cards and eight table rows, photo links still match addresses, the Maps links work, the page reads well at desktop and mobile widths, and the ZIP contains the regenerated page, CSS, and all eight photos.
