```
tests/
├── fixtures/
│   ├── data-section-number/
│   │   ├── output.html
│   │   ├── result-data-section-number.html
│   │   └── test-data-section-number.html
│   ├── test0/
│   │   ├── expected.html
│   │   ├── input.html
│   │   └── output.html
│   ├── test1/
│   │   ├── expected.html
│   │   ├── input.html
│   │   └── output.html
│   ├── test2/
│   │   ├── expected.html
│   │   ├── input.html
│   │   └── output.html
│   ├── test3/
│   │   ├── expected.html
│   │   ├── input.html
│   │   └── output.html
│   └── test4/
│       ├── expected.html
│       ├── input.html
│       └── output.html
├── integration/
│   └── __init__.py
├── unit/
│   ├── lib/
│   │   ├── lineardoc/
│   │   │   ├── data/
│   │   │   │   ├── test-block-template-section-1.html
│   │   │   │   ├── test-block-template-section-2.html
│   │   │   │   ├── test-block-template-section-3.html
│   │   │   │   ├── test-block-template-section-4.html
│   │   │   │   ├── test-chunks-inline.html
│   │   │   │   ├── test-figure-inline.html
│   │   │   │   ├── test-inline-template-section.html
│   │   │   │   ├── test1-result.xhtml
│   │   │   │   ├── test1-result.xml
│   │   │   │   ├── test1.xhtml
│   │   │   │   ├── test2-result.xhtml
│   │   │   │   ├── test2-result.xml
│   │   │   │   ├── test2.xhtml
│   │   │   │   ├── test3-result.xhtml
│   │   │   │   ├── test3-result.xml
│   │   │   │   ├── test3.xhtml
│   │   │   │   ├── test4-result.xhtml
│   │   │   │   ├── test4-result.xml
│   │   │   │   ├── test4.xhtml
│   │   │   │   ├── test5-result.xhtml
│   │   │   │   ├── test5-result.xml
│   │   │   │   ├── test5.xhtml
│   │   │   │   ├── test6-result.xhtml
│   │   │   │   ├── test6-result.xml
│   │   │   │   ├── test6.xhtml
│   │   │   │   ├── test7-result.xhtml
│   │   │   │   ├── test7-result.xml
│   │   │   │   ├── test7.xhtml
│   │   │   │   ├── test8-result.xhtml
│   │   │   │   ├── test8-result.xml
│   │   │   │   ├── test8.xhtml
│   │   │   │   ├── text-inline-template-empty-content.html
│   │   │   │   └── translate.test.json
│   │   │   ├── test_builder.py
│   │   │   ├── test_contextualizer.py
│   │   │   ├── test_doc.py
│   │   │   ├── test_doc_as_js.py
│   │   │   ├── test_doc_item.py
│   │   │   ├── test_doc_wrap_sections.py
│   │   │   ├── test_elements.py
│   │   │   ├── test_lineardoc_utils.py
│   │   │   ├── test_normalizer.py
│   │   │   ├── test_parser.py
│   │   │   ├── test_text_block.py
│   │   │   ├── test_text_chunk.py
│   │   │   └── test_util.py
│   │   └── segmentation/
│   │       ├── data/
│   │       │   ├── audio-inline-result.html
│   │       │   ├── audio-inline-test.html
│   │       │   ├── audio-result.html
│   │       │   ├── audio-test.html
│   │       │   ├── README.md
│   │       │   ├── result-1.html
│   │       │   ├── result-10.html
│   │       │   ├── result-11.html
│   │       │   ├── result-12.html
│   │       │   ├── result-13.html
│   │       │   ├── result-14.html
│   │       │   ├── result-15.html
│   │       │   ├── result-16.html
│   │       │   ├── result-17.html
│   │       │   ├── result-18.html
│   │       │   ├── result-19.html
│   │       │   ├── result-2.html
│   │       │   ├── result-20.html
│   │       │   ├── result-21.html
│   │       │   ├── result-22.html
│   │       │   ├── result-23.html
│   │       │   ├── result-24.html
│   │       │   ├── result-25.html
│   │       │   ├── result-3.html
│   │       │   ├── result-4.html
│   │       │   ├── result-5.html
│   │       │   ├── result-6.html
│   │       │   ├── result-7.html
│   │       │   ├── result-8.html
│   │       │   ├── result-9.html
│   │       │   ├── result-blocklevel-template.html
│   │       │   ├── result-debian-1.html
│   │       │   ├── result-ends-with-bracket.html
│   │       │   ├── result-ends-with-references-missing-letters.html
│   │       │   ├── result-figure-inline-segmentation.html
│   │       │   ├── result-figure-inline.html
│   │       │   ├── result-T213262.html
│   │       │   ├── result-T283513.html
│   │       │   ├── result-T338689.html
│   │       │   ├── result-template-styles.html
│   │       │   ├── result-transclusion-textblock.html
│   │       │   ├── result-transclusioncontext-about.html
│   │       │   ├── test-1.html
│   │       │   ├── test-10.html
│   │       │   ├── test-11.html
│   │       │   ├── test-12.html
│   │       │   ├── test-13.html
│   │       │   ├── test-14.html
│   │       │   ├── test-15.html
│   │       │   ├── test-16.html
│   │       │   ├── test-17.html
│   │       │   ├── test-18.html
│   │       │   ├── test-19.html
│   │       │   ├── test-2.html
│   │       │   ├── test-20.html
│   │       │   ├── test-21.html
│   │       │   ├── test-22.html
│   │       │   ├── test-23.html
│   │       │   ├── test-24.html
│   │       │   ├── test-25.html
│   │       │   ├── test-3.html
│   │       │   ├── test-4.html
│   │       │   ├── test-5.html
│   │       │   ├── test-6.html
│   │       │   ├── test-7.html
│   │       │   ├── test-8.html
│   │       │   ├── test-9.html
│   │       │   ├── test-blocklevel-template.html
│   │       │   ├── test-debian-1.html
│   │       │   ├── test-ends-with-bracket.html
│   │       │   ├── test-ends-with-references-missing-letters.html
│   │       │   ├── test-figure-inline-segmentation.html
│   │       │   ├── test-figure-inline.html
│   │       │   ├── test-T213262.html
│   │       │   ├── test-T283513.html
│   │       │   ├── test-T338689.html
│   │       │   ├── test-template-styles.html
│   │       │   ├── test-transclusion-textblock.html
│   │       │   ├── test-transclusioncontext-about.html
│   │       │   ├── video-inline-result.html
│   │       │   ├── video-inline-test.html
│   │       │   ├── video-result.html
│   │       │   └── video-test.html
│   │       ├── output/
│   │       │   ├── audio-inline-result.html
│   │       │   ├── audio-result.html
│   │       │   ├── result-1.html
│   │       │   ├── result-10.html
│   │       │   ├── result-11.html
│   │       │   ├── result-12.html
│   │       │   ├── result-13.html
│   │       │   ├── result-14.html
│   │       │   ├── result-15.html
│   │       │   ├── result-16.html
│   │       │   ├── result-17.html
│   │       │   ├── result-18.html
│   │       │   ├── result-19.html
│   │       │   ├── result-2.html
│   │       │   ├── result-20.html
│   │       │   ├── result-21.html
│   │       │   ├── result-22.html
│   │       │   ├── result-23.html
│   │       │   ├── result-24.html
│   │       │   ├── result-25.html
│   │       │   ├── result-3.html
│   │       │   ├── result-4.html
│   │       │   ├── result-5.html
│   │       │   ├── result-6.html
│   │       │   ├── result-7.html
│   │       │   ├── result-8.html
│   │       │   ├── result-9.html
│   │       │   ├── result-blocklevel-template.html
│   │       │   ├── result-debian-1.html
│   │       │   ├── result-ends-with-bracket.html
│   │       │   ├── result-ends-with-references-missing-letters.html
│   │       │   ├── result-figure-inline-segmentation.html
│   │       │   ├── result-figure-inline.html
│   │       │   ├── result-T213262.html
│   │       │   ├── result-T283513.html
│   │       │   ├── result-T338689.html
│   │       │   ├── result-template-styles.html
│   │       │   ├── result-transclusion-textblock.html
│   │       │   ├── result-transclusioncontext-about.html
│   │       │   ├── video-inline-result.html
│   │       │   └── video-result.html
│   │       ├── SegmentationTests.json
│   │       ├── test_cx_segmenter.py
│   │       ├── test_cx_segmenter_remove_url.py
│   │       └── test_segmenter.py
│   ├── processor/
│   │   ├── test_comprehensive.py
│   │   ├── test_processing.py
│   │   ├── test_processor.py
│   │   └── test_processor_unit.py
│   ├── utils/
│   │   └── assert.js
│   ├── __init__.py
│   └── html_normalizer.py
├── __init__.py
├── conftest.py
├── lib
└── README.md

```