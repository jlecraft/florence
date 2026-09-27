from pathlib import Path
from html import escape
from base64 import b64encode
from hashlib import sha256
from urllib.parse import quote
from zipfile import ZipFile, ZIP_DEFLATED
p=Path(__file__).parent
homes=[
('Storage Galore','',505000,2,2,1636,'2265 24th St','48439691','Room for more.','Modern updates with incredible storage and strong layout. Great yard. Won\'t get any real use from the RV port.','2265-24th-St',False,'Public','Public sewer',3422,'0.28 acres',1976,'177382071'),
('Lake Cabin','',459900,2,2,1336,'83362 Parkway Dr','48425879','Cabin days, coastal evenings.','Cozy wood paneling, great back yard. Shared office for us with the bonus room. Of note is community water, but research shows the supplier is trustworthy.','83362-Parkway-Dr',False,'Community','Septic tank',2333,'0.45 acres',1969,'745319223'),
('Kitchen Hearth','',399000,4,2,1630,'5590 S Shore Dr','48406087','Twice the fireside charm.','On the market for a LONG time. Photos out of date and unsure of the status of updates like paint and flooring. Love the fireplace placement and general layout.','5590-S-Shore-Dr',False,'Public','Septic tank',2690,'0.24 acres',1978,'152806514'),
('Boat House','',395000,2,2,1512,'89555 Shore Crest Dr','459164352','Space for the next adventure.','Cool location, but have questions about manufactured history and foundation.','89555-Shore-Crest-Dr',True,'Public','Standard septic',3353,'0.32 acres',2019,'270810465'),
('Beach House','',429000,3,2,1586,'4792 Rhododendron Loop','306216648','A place to make our own.','In Heceta beach area. Brick fireplace. Nice yeard. 1.5 miles to beach. Manufactured with questions about foundation. Can the subfloor support something other than carpeting?','4792-Rhododendron-Loop',True,'Public','Standard septic',2255,'0.43 acres',1996,'415050331'),
('River House','',439500,3,2,1396,'240 11th St','48422880','An already-furnished possibility.','Current AirBnB rental that includes furnishing. Smaller lot. Vinyl flooring throughout. May get noise from road.','240-11th-St',False,'Public','Public sewer',3053,'0.19 acres',1990,'145264700'),
('Funky Stove','',438900,3,2,1444,'2286 N 22nd Ct','48454541','A cozy place to gather.','Smaller lot and closer to neighbors in east Florence.','2286-N-22nd-Ct',False,'Public','Public sewer',3267,'0.22 acres',1989,'142060824'),
('Double Gas Fireplace','',525000,3,2,1705,'5045 N Loftus Rd','48425417','Warmth at the center.','Well and septic on a gravel road. Good acreage. Extra shed. Some carpet. Source for gas fireplace?','5045-N-Loftus-Rd',False,'Well','Standard septic',2454,'0.70 acres',1950,'183278526')]
cards=[]; rows=[]
for i,(name,status,price,beds,baths,sqft,address,zpid,tag,note,slug,manufactured,water,sewer,taxes,lot,year,mls) in enumerate(homes,1):
 url=f'https://www.zillow.com/homedetails/{slug}-Florence-OR-97439/{zpid}_zpid/'
 maps_url=f'https://www.google.com/maps/search/?api=1&query={quote(f"{address}, Florence, OR 97439", safe="")}'
 details=''.join(f'<div><dt>{label}</dt><dd>{escape(str(value))}</dd></div>' for label,value in [('Manufactured','Yes' if manufactured else 'No'),('Water',water),('Sewage',sewer),('2025 taxes',f'${taxes:,}/year'),('Lot size',lot),('Year built',year)])
 details += f'<div><dt>MLS</dt><dd>#{escape(mls)}</dd></div>'
 cards.append(f'''<article class="home" id="home-{i}"><div class="photo"><a class="photo-link" href="{url}" target="_blank" rel="noopener noreferrer" aria-label="View listing for {escape(address)} (opens in a new tab)"><img src="assets/{i:02}.jpg" alt="Listing exterior of {escape(address)}" width="960" height="640" {'fetchpriority="high"' if i==1 else 'loading="eager"'}></a><span class="rank">{i:02}</span>{'<span class="status">Sale pending</span>' if status else ''}</div><div class="home-body"><div class="eyebrow">{'FIRST CHOICE' if i==1 else f'PREFERENCE {i:02}'}</div><h3>{escape(name)}</h3><p class="address"><a href="{escape(maps_url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(address)} · Florence, OR 97439</a></p><div class="price">${price:,}<span>asking price</span></div><div class="facts"><span><b>{beds}</b> bedrooms</span><span><b>{baths}</b> {'bathroom' if baths==1 else 'bathrooms'}</span><span><b>{sqft:,}</b> sq ft</span></div><dl class="property-details">{details}</dl><div class="note"><span>NOTES</span><p>{escape(note)}</p></div></div></article>''')
 lot_sqft=round(float(lot.split()[0].replace(',','')) * 43560) if 'acre' in lot else int(lot.split()[0].replace(',',''))
 built=f'<em title="Manufactured home">{year}</em>' if manufactured else str(year)
 rows.append(f'<tr><td class="table-rank" data-sort-value="{i}">{i:02}</td><th scope="row" data-sort-value="{escape(name, quote=True)}"><a href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(name)}</a></th><td class="table-address" data-sort-value="{escape(address, quote=True)}"><a href="{escape(maps_url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(address)}<br><span class="table-city">Florence, OR 97439</span></a></td><td data-sort-value="{price}">${price:,}</td><td data-sort-value="{beds*100+baths}">{beds}/{baths}</td><td data-sort-value="{sqft}">{sqft:,}</td><td data-sort-value="{escape(water, quote=True)}">{escape(water)}</td><td data-sort-value="{escape(sewer, quote=True)}">{escape(sewer)}</td><td data-sort-value="{taxes}">${taxes:,}</td><td data-sort-value="{lot_sqft}">{escape(lot)}</td><td data-sort-value="{year}">{built}</td></tr>')
html='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#151c1a"><meta name="description" content="Eight Florence, Oregon homes in preference order. Photos, asking prices, bedrooms, bathrooms, and the details we remember."><title>Florence, Oregon</title><link rel="stylesheet" href="style.css"></head><body><a class="skip" href="#shortlist">Skip to homes</a><header class="simple-header"><h1>Florence, Oregon</h1></header><main><section id="shortlist" class="shortlist"><div class="section-heading"><div><p class="eyebrow">FLORENCE HOME LISTINGS</p><h2>Home shortlist<span>.</span></h2></div><p>01 — 08 <span>Listed in preference order</span></p></div><div class="grid">'''+''.join(cards)+'''</div></section><section id="compare" class="comparison"><div class="section-heading"><div><p class="eyebrow">THE DETAILS, SIDE BY SIDE</p><h2>At a glance<span>.</span></h2></div><a href="#shortlist">Back to the homes ↑</a></div><div class="table-scroll" tabindex="0" role="region" aria-label="Home comparison table, scroll horizontally on small screens"><table><thead><tr><th scope="col">Rank</th><th scope="col">The home</th><th scope="col">Asking price</th><th scope="col">Beds</th><th scope="col">Baths</th><th scope="col">Sq ft</th></tr></thead><tbody>'''+''.join(rows)+'''</tbody></table></div></section><aside class="details"><span class="eyebrow">A NOTE ON THE DETAILS</span><p>Listing information retrieved September 26, 2026 from the linked Zillow pages; Armstrong Way uses the newer September listing on Redfin. These are asking prices, not estimates of value. Prices and availability may change. “Sale pending” is our note for Pole barn. Home nicknames and notes are informal and do not imply waterfront access.</p><p>Photos courtesy of the linked property listings; Armstrong Way photo via RMLS / Keith McCue Realty.</p></aside></main><footer><span>FLORENCE, OREGON</span><a href="#">Back to top ↑</a></footer></body></html>'''
column_labels=[('Rank','number'),('The home','text'),('Street address','text'),('Asking price','number'),('Rooms','number'),('Sq ft','number'),('Water','text'),('Sewage','text'),('2025 taxes','number'),('Lot size','number'),('Built','number')]
table_headers=[]
for index,(label,kind) in enumerate(column_labels):
 aria_sort=' aria-sort="ascending"' if index==0 else ''
 help_icon='<span class="rooms-help" tabindex="0" aria-describedby="rooms-tip" aria-label="Rooms format">i<span id="rooms-tip" class="rooms-tip" role="tooltip">Bedrooms / bathrooms (3/2 means 3 bedrooms, 2 bathrooms)</span></span>' if label=='Rooms' else ''
 table_headers.append(f'<th scope="col"{aria_sort}><button type="button" class="sort-button" data-sort-type="{kind}">{label}</button>{help_icon}</th>')
html=html.replace(
 'Photos, asking prices, bedrooms, bathrooms, and the details we remember.',
 'Prices, taxes, lot sizes, water, sewage, and construction details.'
)
html=html.replace(
 '<th scope="col">Rank</th><th scope="col">The home</th><th scope="col">Asking price</th><th scope="col">Beds</th><th scope="col">Baths</th><th scope="col">Sq ft</th>',
 ''.join(table_headers)
)
html=html.replace(
 'Listing information retrieved September 26, 2026 from the linked Zillow pages; Armstrong Way uses the newer September listing on Redfin. These are asking prices, not estimates of value. Prices and availability may change. “Sale pending” is our note for Pole barn. Home nicknames and notes are informal and do not imply waterfront access.',
 "Listing details were checked September 26, 2026. Beach House's $429,000 asking price reflects a September 22 MLS reduction; its linked Zillow property record may show an estimate instead of the listing price. Taxes are 2025 property taxes, rounded to whole dollars; future bills may differ. Prices, details, and availability may change. For Rhododendron Loop, the MLS record identifies it as manufactured and gives its utilities and 2025 taxes; Zillow shows older, conflicting details. Home nicknames and notes are informal and do not imply waterfront access."
)
html=html.replace(
 'Photos courtesy of the linked property listings; Armstrong Way photo via RMLS / Keith McCue Realty.',
 'Photos courtesy of the linked property listings. Storage Galore and Funky Stove photos are via RMLS / Redfin.'
)
html=html.replace('</table></div></section><aside class="details">','</table></div><p class="table-note"><em>Italic year</em> indicates a manufactured home. Select a column heading to sort.</p></section><aside class="details">')
sort_script='''
const comparisonTable = document.querySelector('#compare table');
const tableBody = comparisonTable.tBodies[0];
const sortButtons = comparisonTable.querySelectorAll('.sort-button');

sortButtons.forEach(button => {
  button.addEventListener('click', () => {
    const heading = button.closest('th');
    const column = heading.cellIndex;
    const direction = heading.getAttribute('aria-sort') === 'ascending' ? -1 : 1;
    const rows = Array.from(tableBody.rows);

    rows.sort((left, right) => {
      const leftValue = left.cells[column].dataset.sortValue;
      const rightValue = right.cells[column].dataset.sortValue;
      const difference = button.dataset.sortType === 'number'
        ? Number(leftValue) - Number(rightValue)
        : leftValue.localeCompare(rightValue, undefined, {sensitivity: 'base'});
      return difference * direction || Number(left.cells[0].dataset.sortValue) - Number(right.cells[0].dataset.sortValue);
    });

    comparisonTable.querySelectorAll('thead th').forEach(cell => cell.removeAttribute('aria-sort'));
    heading.setAttribute('aria-sort', direction === 1 ? 'ascending' : 'descending');
    tableBody.append(...rows);
  });
});
'''
html=html.replace('</body>',f'<script>{sort_script}</script></body>')
style=(p/'style.css').read_text()
stylesheet_href=f'style.css?v={sha256(style.encode()).hexdigest()[:12]}'
html=html.replace('href="style.css"',f'href="{stylesheet_href}"')
(p/'index.html').write_text(html)

# Keep the single-file page and the download bundle aligned with index.html.
self_contained=html.replace(f'<link rel="stylesheet" href="{stylesheet_href}">',f'<style>{style}</style>')
for i in range(1,len(homes)+1):
 photo=(p/'assets'/f'{i:02}.jpg').read_bytes()
 self_contained=self_contained.replace(f'assets/{i:02}.jpg',f'data:image/jpeg;base64,{b64encode(photo).decode("ascii")}')
(p/'Florence-Homes.html').write_text(self_contained)
with ZipFile(p/'florence-homes.zip','w',compression=ZIP_DEFLATED) as bundle:
 for path in ['index.html','style.css']+[f'assets/{i:02}.jpg' for i in range(1,len(homes)+1)]:
  bundle.write(p/path,path)
