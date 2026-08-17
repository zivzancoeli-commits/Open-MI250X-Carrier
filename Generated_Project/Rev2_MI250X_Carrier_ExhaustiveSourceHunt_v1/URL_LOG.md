# URL_LOG — exhaustive hunt 2026-08-17

Agent UA: `Mozilla/5.0 … Chrome/124 … Open-MI250X-Carrier-research`  
Format: `HTTP|content-type|bytes|url -> saved_as`

Cloudflare/WAF HTML saved as the named file is **not** the intended PDF/xlsx. Wayback **498** bodies are 548-byte HTML, not spreadsheets.

## Molex / distributors

```
200|application/pdf|34595  https://www.farnell.com/datasheets/3919676.pdf  ->  Farnell_Molex_2189101115.pdf
0|timeout|0  https://www.molex.com/en-us/products/part-detail/2189101115  ->  (no file)
0|timeout|0  https://www.molex.com/pdm_docs/ps/2189100001-PS.pdf
0|timeout|0  https://www.molex.com/pdm_docs/ps/2189100001-PS-000.pdf
0|timeout|0  https://www.molex.com/pdm_docs/ps/PS-218910-0001.pdf
0|timeout|0  https://www.molex.com/pdm_docs/sd/2189101115.pdf
0|timeout|0  https://www.molex.com/pdm_docs/sd/2189101115-SD.pdf
0|timeout|0  https://www.molex.com/pdm_docs/sd/2189101115-SD-000.pdf
0|timeout|0  https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/218/218910/2189101115.pdf
0|timeout|0  https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/3dcadmodelspdf/218/218910/2189101115.pdf
0|timeout|0  https://www.molex.com/content/dam/molex/molex-dot-com/en_us/pdf/datasheets/987652-0673.pdf
0|timeout|0  https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/pdf/datasheets/987652-0673.pdf
000|http1.1 fail|0  same molex.com URLs retried with --http1.1
200|application/pdf|1335124  https://www.content.molex.com/dxresources/1b7b/1b7b49e5-2def-4843-a9ed-656713e84952.pdf  ->  Molex_Mirror_Mezz_overview.pdf
200|application/pdf|326192  https://www.content.molex.com/dxresources/3d6e/3d6e8b6f-430d-49cd-b843-a6374232eb3c.pdf  ->  Molex_Mirror_Mezz_15x11_OCP.pdf
200|application/pdf|318701  https://www.content.molex.com/dxresources/7f7b/7f7b6bdf-bb6d-4339-b836-185ec7a3b999.pdf  ->  Molex_Supports_OCP_Open_Standards.pdf
200|application/pdf|1448968  https://www.content.molex.com/dxresources/b3b7/b3b7bc64-a2fc-4845-90bd-f1efb35a3ffb.pdf  ->  Molex_Mirror_Mezz_15x11_OCP_connectors.pdf
403|text/html|5900  https://www.digikey.com/en/products/detail/molex/2189101115/16695784  ->  DigiKey_2189101115.html
200|text/html|13895  https://www.mouser.com/ProductDetail/Molex/218910-1115  ->  Mouser_218910-1115.html  (JS shell)
403|text/html|234  https://www.newark.com/molex/2189101115/connector-mezz-15pos-11row/dp/88AH6546  ->  Newark_2189101115.html
403|text/html|50853  https://octopart.com/218910-1115-molex-110847315  ->  Octopart_2189101115.html
000|fail|0  https://www.arrow.com/en/products/2189101115/molex
200|text/html|428323  https://www.lcsc.com/product-detail/Board-to-Board-and-Backplane-Connector_Molex-2189101115_C22464012.html  ->  LCSC_2189101115.html  (WRONG SKU image; discarded)
403|text/html|61397  https://www.studocu.com/tw/document/university-of-taipei/learning-and-materials-design/product-specification-document-psd-2189101115-sd-for-molex/150171610
```

## OCP / Wayback / files.opencompute.org

```
403|text/html|5799  http://files.opencompute.org/oc/public.php?service=files&t=938c61e5b1d3c5c2b5c33f95525b1412
403|text/html|5799  http://files.opencompute.org/oc/public.php?service=files&t=fb91baceba6c1dfaa9dc5531365b4f45
498|text/html|548  https://web.archive.org/web/20211205194306/http://files.opencompute.org/oc/public.php?service=files&t=938c61e5b1d3c5c2b5c33f95525b1412&download&path=//OAM%20Pin%20map%20rev%201.0.xlsx
498|text/html|548  https://web.archive.org/web/20220421131015/http://files.opencompute.org/oc/public.php?service=files&t=938c61e5b1d3c5c2b5c33f95525b1412&download&path=//OAM%20Pin%20map%20rev%201.0.xlsx
498|text/html|548  https://web.archive.org/web/20211205210451/http://files.opencompute.org/oc/public.php?service=files&t=fb91baceba6c1dfaa9dc5531365b4f45&download&path=//oam_pin%20list_rev1.1.xlsx
498|text/html|548  https://web.archive.org/web/20221225104050/http://files.opencompute.org/oc/public.php?service=files&t=fb91baceba6c1dfaa9dc5531365b4f45&download&path=//oam_pin%20list_rev1.1.xlsx
498|text/html|548  https://web.archive.org/web/20200924024102/http://files.opencompute.org/oc/public.php?service=files&t=938c61e5b1d3c5c2b5c33f95525b1412&download&path=//OAM_Pin%20list_Rev1.0.xlsx
498|text/html|548  https://web.archive.org/web/2023/https://www.opencompute.org/wiki/Server/OAI
498|text/html|548  https://web.archive.org/web/20220224000000/https://www.opencompute.org/documents/universal-baseboard-design-specification-v1p5-final-20220223-docx-pdf
CDX 503  files.opencompute.org/*Pin*map*
CDX 503  files.opencompute.org/*OAM*Pin*
CDX 503  files.opencompute.org/*pin*list*
CDX 200  *.opencompute.org/*v1p5*  (unrelated 2011 homepage hits; not v1.5 PDF)
CDX 503  www.molex.com/pdm_docs/ps/218910*
CDX 503  www.molex.com/*2189100001*
CDX 200  www.molex.com/*2189101115*  (0 captures)
curl  (Cloudflare challenge)  https://www.opencompute.org/documents/ocp-accelerator-module-design-specification-v1p5-final-20220223-docx-1-pdf
curl  (Cloudflare challenge)  https://www.opencompute.org/documents/universal-baseboard-design-specification-v1p5-final-20220223-docx-pdf
WebSearch pipeline  (full PDF text)  same two OCP URLs + OAM v1.0/v1.1 + r2.0 (r2.0 unused)
200|application/pdf|2980981  https://146a55aca6f00848c565-a7635525d40ac1c70300198708936b4e.ssl.cf1.rackcdn.com/images/18a84b960d9b11bb2fbc9a4d59f09fc01086d9b7.pdf  ->  OCP_OAI_lightning_2019.pdf
200|text/html|259164  https://github.com/opencomputeproject/OCP-SVR-OAI-Open_Accelerator_Infrastructure
200|text/html|172167  https://github.com/search?q=OAM_Pin_map_rev1.0&type=code  (result_count: 0)
200|text/html|3489  https://ocp-all.groups.io/g/OCP-OAI/topic/ocp_oai_june_updates/83416097
gh search code  HTTP 429 (rate limit)  OAM_Pin_map_rev / 218910-1115 / "OCP Generic Pin Map"
```

## AMD / Instinct / ROCm

```
200|application/pdf|1011276  https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/instinct-mi200-datasheet.pdf
200|text/html|182391  https://www.amd.com/en/products/accelerators/instinct/mi200/mi250x.html
200|text/html|63148  https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi250.html
200|text/html|43437  https://instinct.docs.amd.com/latest/gpu-arch/mi250.html
404|text/html|41995  https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch/mi250.html
404|text/html|146099  https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/white-papers/amd-cdna2-white-paper.pdf
```

## OEM / donors / cooling / PCIe

```
403|text/html|426  https://www.supermicro.com/datasheet/datasheet_H12_UniversalGPU.pdf
403|text/html|425  https://www.supermicro.com/manuals/superserver/4U/MNL-2507.pdf
403|text/html|437  https://www.supermicro.com/en/products/system/datasheet/as-4124gq-tnmi
200|application/pdf|481914  https://download.gigabyte.com/FileList/DataSheet/G492-HA0_datasheet_v1.0.pdf?v=129fb2ffe0516214804c84cee6152fbd
200|application/pdf|909573  https://i-wave.com/wp-content/uploads/0124-MCIO.pdf
200|text/html|45784  https://www.ti.com/tool/CEM2SLIMSAS-EVM
200|application/pdf|604684  https://www.ti.com/lit/ug/snlu278/snlu278.pdf
200|text/html|118083  https://c-payne.com/products/pcie-slimsas-host-adapter-x16-to-2-8i-straight-aic
200|text/html|558099  https://www.microsatacables.com/pcie-x16-gen4-with-redriver-to-slimsas-8i-dual-port-aic
200|text/html|33671  https://www.wiredzone.com/shop/product/10026107-supermicro-cbl-mcio-1278s5fyb1-cable-kit-for-gpu-mi-200-11129
200|text/html|434014  https://forum.level1techs.com/t/someone-needs-to-figure-out-how-to-adapt-mi250-gpus-to-pcie/250596
200|text/html|97158  https://engineering.fb.com/2019/03/14/data-center-engineering/accelerator-modules/
200|text/html|126396  https://www.itcreations.com/product/150032
403|text/html|5525  https://alinc.com/sps-pca-mi250x-oam-mcm-spl-accelerator-p41933-001
200|text/html|166272  https://www.servethehome.com/amd-mi250x-and-toplogies-explained-at-hc34-hpe-gigabyte-supermicro/
200|text/html|334767  https://sendcutsend.com/services/hardware/
403|text/html|5595  https://www.amphenol-cs.com/product-series/airmax.html
200|text/html|860111  https://www.penguincomputing.com/
000|fail|0  https://www.hpe.com/psnow/doc/a00114819enw
200|text/html|32849  https://grabcad.com/library?page=1&time=all_time&sort=recent&query=OAM%20UBB
200|application/pdf|461137  https://www.meanwell.com/Upload/PDF/RCP-2000/RCP-2000-SPEC.PDF
```

## archive.org advancedsearch

```
000|TLS reset|0  https://archive.org/advancedsearch.php?q=%22OAM%20Pin%20map%22...
200|json|~  https://archive.org/advancedsearch.php?q=%22Universal%20Baseboard%20Design%20Specification%22  (numFound 0 in parsed body)
```

## License note

Saved PDFs are vendor public datasheets/marketing (Molex CDN, Farnell, AMD, MEAN WELL, TI, i-wave, Gigabyte, OCP 2019 lightning-talk CDN). OCP v1.5 **binary** PDFs were not stored (Cloudflare). Extracted OCP text already present in-repo under FullSend is copied here for this tree. Do not treat 403/498 HTML as the named document.
