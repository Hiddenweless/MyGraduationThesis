# DSE Submission Checklist

This checklist is for the Springer Nature journal *Data Science and Engineering*.

## Files prepared

- `sn-article.tex`: anonymous main manuscript.
- `sn-bibliography.bib`: bibliography used by the main manuscript.
- `sn-article.bbl`: generated bibliography file for submission systems that request compiled bibliography output.
- `title-page.tex`: separate title page with author, affiliation, corresponding author, funding, acknowledgement, contribution, data availability, and code availability information.
- `sn-article.pdf`: compiled anonymous main manuscript.
- `title-page.pdf`: compiled title page.
- `figures/*.pdf`: manuscript figures used by the anonymous main manuscript.

## Official requirements checked

- Double-blind review: the main manuscript uses anonymous author metadata and omits acknowledgements, funding, and author contribution details.
- Abstract length: the abstract is approximately 221 words, within the common 150-250 word range stated in the DSE instructions.
- Keywords: six keywords are provided.
- Declarations: funding, competing interests, ethics, consent, data availability, code availability, and author contribution sections are present.
- Template: the manuscript uses the official Springer Nature `sn-jnl` LaTeX class from the downloaded package.
- Bibliography: the manuscript uses `sn-bibliography.bib` and the Springer Nature numeric math/physical sciences style.

## Items requiring final author confirmation

- Final approval of the author order, corresponding author, email addresses, and affiliations.
- Final approval of the funding, acknowledgement, author contribution, data availability, and code availability statements.
- Final confirmation that the experiment numbers are final and can be reported as journal results.
- Whether all co-authors approve submitting to *Data Science and Engineering* and paying/waiving the open-access article processing charge.

## Two-round review log

- Round 1 completed: the first compile exposed a BibTeX style-path issue because BibTeX did not search the `bst/` subdirectory. The official `.bst` files were copied to the template root, and the manuscript was recompiled successfully.
- Round 1 fixes completed: the main manuscript was rewritten in the Springer Nature template, the bibliography was reduced to cited entries, and required figures were copied into the template directory.
- Round 2 completed: the manuscript was checked for double-blind compliance, missing citations, missing cross-references, missing figures, declaration sections, abstract length, keyword count, and template compatibility.
- Round 2 fixes completed: declaration headings were normalized, figure inclusions were switched to generated PNG files for cleaner PDF compilation, and the separate title page was made independently compilable.
- Final compile status: `sn-article.pdf` and `title-page.pdf` both compile. Final logs contain no undefined citations, no undefined cross-references, no missing figures, no LaTeX errors, and no overfull boxes. Only harmless font substitution warnings remain from the Springer Nature class.

## Layout verification

- The anonymous submission manuscript intentionally keeps the default Springer Nature authoring-template layout, which is single-column unless the `iicol` option is added.
- Published *Data Science and Engineering* PDFs are typeset by Springer in a two-column production layout. This does not mean the initial LaTeX submission must be two-column.
- The apparent left/right margin difference comes from the official `sn-jnl.cls` settings: it loads a two-sided layout with a `bindingoffset`, so odd and even pages mirror their inner and outer margins.
- A separate two-column preview was generated in `dse-two-column-preview/` using the official `iicol` option for visual comparison, but it is kept outside the clean submission package to avoid confusing the default submission files.
