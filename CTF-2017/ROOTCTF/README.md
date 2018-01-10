# ROOTCTF 2017 WriteUp
<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=ks_c_5601-1987">
<meta name=ProgId content=Word.Document>
<meta name=Generator content="Microsoft Word 15">
<meta name=Originator content="Microsoft Word 15">
<link rel=File-List href="README.files/filelist.xml">
<link rel=Edit-Time-Data href="README.files/editdata.mso">
<!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
w\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]--><!--[if gte mso 9]><xml>
 <o:DocumentProperties>
  <o:Author>준호네</o:Author>
  <o:LastAuthor>JunhoYeo</o:LastAuthor>
  <o:Revision>3</o:Revision>
  <o:TotalTime>146</o:TotalTime>
  <o:Created>2018-01-09T14:40:00Z</o:Created>
  <o:LastSaved>2018-01-09T14:40:00Z</o:LastSaved>
  <o:Pages>1</o:Pages>
  <o:Words>1525</o:Words>
  <o:Characters>8694</o:Characters>
  <o:Lines>72</o:Lines>
  <o:Paragraphs>20</o:Paragraphs>
  <o:CharactersWithSpaces>10199</o:CharactersWithSpaces>
  <o:Version>16.00</o:Version>
 </o:DocumentProperties>
 <o:OfficeDocumentSettings>
  <o:RelyOnVML/>
  <o:AllowPNG/>
 </o:OfficeDocumentSettings>
</xml><![endif]-->
<link rel=dataStoreItem href="README.files/item0001.xml"
target="README.files/props002.xml">
<link rel=themeData href="README.files/themedata.thmx">
<link rel=colorSchemeMapping
href="README.files/colorschememapping.xml">
<!--[if gte mso 9]><xml>
 <w:WordDocument>
  <w:TrackMoves>false</w:TrackMoves>
  <w:TrackFormatting/>
  <w:DisplayHorizontalDrawingGridEvery>0</w:DisplayHorizontalDrawingGridEvery>
  <w:DisplayVerticalDrawingGridEvery>2</w:DisplayVerticalDrawingGridEvery>
  <w:ValidateAgainstSchemas/>
  <w:SaveIfXMLInvalid>false</w:SaveIfXMLInvalid>
  <w:IgnoreMixedContent>false</w:IgnoreMixedContent>
  <w:AlwaysShowPlaceholderText>false</w:AlwaysShowPlaceholderText>
  <w:DoNotPromoteQF/>
  <w:LidThemeOther>EN-US</w:LidThemeOther>
  <w:LidThemeAsian>KO</w:LidThemeAsian>
  <w:LidThemeComplexScript>X-NONE</w:LidThemeComplexScript>
  <w:Compatibility>
   <w:SpaceForUL/>
   <w:BalanceSingleByteDoubleByteWidth/>
   <w:DoNotLeaveBackslashAlone/>
   <w:ULTrailSpace/>
   <w:DoNotExpandShiftReturn/>
   <w:AdjustLineHeightInTable/>
   <w:BreakWrappedTables/>
   <w:SnapToGridInCell/>
   <w:WrapTextWithPunct/>
   <w:UseAsianBreakRules/>
   <w:DontGrowAutofit/>
   <w:SplitPgBreakAndParaMark/>
   <w:EnableOpenTypeKerning/>
   <w:DontFlipMirrorIndents/>
   <w:OverrideTableStyleHps/>
   <w:UseFELayout/>
  </w:Compatibility>
  <m:mathPr>
   <m:mathFont m:val="Cambria Math"/>
   <m:brkBin m:val="before"/>
   <m:brkBinSub m:val="&#45;-"/>
   <m:smallFrac m:val="off"/>
   <m:dispDef/>
   <m:lMargin m:val="0"/>
   <m:rMargin m:val="0"/>
   <m:defJc m:val="centerGroup"/>
   <m:wrapIndent m:val="1440"/>
   <m:intLim m:val="subSup"/>
   <m:naryLim m:val="undOvr"/>
  </m:mathPr></w:WordDocument>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <w:LatentStyles DefLockedState="false" DefUnhideWhenUsed="false"
  DefSemiHidden="false" DefQFormat="false" DefPriority="99"
  LatentStyleCount="375">
  <w:LsdException Locked="false" Priority="0" QFormat="true" Name="Normal"/>
  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 1"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 2"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 3"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 4"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 5"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 6"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 7"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 8"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 9"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 9"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 1"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 2"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 3"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 4"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 5"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 6"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 7"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 8"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 9"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footnote text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="header"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footer"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index heading"/>
  <w:LsdException Locked="false" Priority="35" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="caption"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="table of figures"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="envelope address"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="envelope return"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footnote reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="line number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="page number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="endnote reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="endnote text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="table of authorities"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="macro"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="toa heading"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 5"/>
  <w:LsdException Locked="false" Priority="10" QFormat="true" Name="Title"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Closing"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Signature"/>
  <w:LsdException Locked="false" Priority="1" SemiHidden="true"
   UnhideWhenUsed="true" Name="Default Paragraph Font"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Message Header"/>
  <w:LsdException Locked="false" Priority="11" QFormat="true" Name="Subtitle"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Salutation"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Date"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text First Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text First Indent 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Note Heading"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Block Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Hyperlink"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="FollowedHyperlink"/>
  <w:LsdException Locked="false" Priority="22" QFormat="true" Name="Strong"/>
  <w:LsdException Locked="false" Priority="20" QFormat="true" Name="Emphasis"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Document Map"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Plain Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="E-mail Signature"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Top of Form"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Bottom of Form"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal (Web)"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Acronym"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Address"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Cite"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Code"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Definition"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Keyboard"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Preformatted"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Sample"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Typewriter"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Variable"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal Table"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation subject"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="No List"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Contemporary"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Elegant"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Professional"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Subtle 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Subtle 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Balloon Text"/>
  <w:LsdException Locked="false" Priority="39" Name="Table Grid"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Theme"/>
  <w:LsdException Locked="false" SemiHidden="true" Name="Placeholder Text"/>
  <w:LsdException Locked="false" Priority="1" QFormat="true" Name="No Spacing"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 1"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 1"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 1"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 1"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 1"/>
  <w:LsdException Locked="false" SemiHidden="true" Name="Revision"/>
  <w:LsdException Locked="false" Priority="34" QFormat="true"
   Name="List Paragraph"/>
  <w:LsdException Locked="false" Priority="29" QFormat="true" Name="Quote"/>
  <w:LsdException Locked="false" Priority="30" QFormat="true"
   Name="Intense Quote"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 1"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 1"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 1"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 1"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 1"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 2"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 2"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 2"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 2"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 2"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 2"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 2"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 3"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 3"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 3"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 3"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 3"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 3"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 3"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 4"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 4"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 4"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 4"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 4"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 4"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 4"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 5"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 5"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 5"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 5"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 5"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 5"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 5"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 6"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 6"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 6"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 6"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 6"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 6"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 6"/>
  <w:LsdException Locked="false" Priority="19" QFormat="true"
   Name="Subtle Emphasis"/>
  <w:LsdException Locked="false" Priority="21" QFormat="true"
   Name="Intense Emphasis"/>
  <w:LsdException Locked="false" Priority="31" QFormat="true"
   Name="Subtle Reference"/>
  <w:LsdException Locked="false" Priority="32" QFormat="true"
   Name="Intense Reference"/>
  <w:LsdException Locked="false" Priority="33" QFormat="true" Name="Book Title"/>
  <w:LsdException Locked="false" Priority="37" SemiHidden="true"
   UnhideWhenUsed="true" Name="Bibliography"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="TOC Heading"/>
  <w:LsdException Locked="false" Priority="41" Name="Plain Table 1"/>
  <w:LsdException Locked="false" Priority="42" Name="Plain Table 2"/>
  <w:LsdException Locked="false" Priority="43" Name="Plain Table 3"/>
  <w:LsdException Locked="false" Priority="44" Name="Plain Table 4"/>
  <w:LsdException Locked="false" Priority="45" Name="Plain Table 5"/>
  <w:LsdException Locked="false" Priority="40" Name="Grid Table Light"/>
  <w:LsdException Locked="false" Priority="46" Name="Grid Table 1 Light"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark"/>
  <w:LsdException Locked="false" Priority="51" Name="Grid Table 6 Colorful"/>
  <w:LsdException Locked="false" Priority="52" Name="Grid Table 7 Colorful"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 1"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 1"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 1"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 2"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 2"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 2"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 3"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 3"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 3"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 4"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 4"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 4"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 5"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 5"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 5"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 6"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 6"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 6"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="46" Name="List Table 1 Light"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark"/>
  <w:LsdException Locked="false" Priority="51" Name="List Table 6 Colorful"/>
  <w:LsdException Locked="false" Priority="52" Name="List Table 7 Colorful"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 1"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 1"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 1"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 2"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 2"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 2"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 3"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 3"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 3"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 4"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 4"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 4"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 5"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 5"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 5"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 6"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 6"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 6"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Mention"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Smart Hyperlink"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Hashtag"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Unresolved Mention"/>
 </w:LatentStyles>
</xml><![endif]-->
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:굴림;
	panose-1:2 11 6 0 0 1 1 1 1 1;
	mso-font-alt:Gulim;
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:variable;
	mso-font-signature:-1342176593 1775729915 48 0 524447 0;}
@font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:roman;
	mso-font-pitch:variable;
	mso-font-signature:-536869121 1107305727 33554432 0 415 0;}
@font-face
	{font-family:Calibri;
	panose-1:2 15 5 2 2 2 4 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:-536859905 -1073732485 9 0 511 0;}
@font-face
	{font-family:"맑은 고딕";
	panose-1:2 11 5 3 2 0 0 2 0 4;
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:variable;
	mso-font-signature:-1879048145 701988091 18 0 524289 0;}
@font-face
	{font-family:굴림체;
	panose-1:2 11 6 9 0 1 1 1 1 1;
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:fixed;
	mso-font-signature:-1342176593 1775729915 48 0 524447 0;}
@font-face
	{font-family:"나눔고딕 ExtraBold";
	panose-1:2 13 9 4 0 0 0 0 0 0;
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:variable;
	mso-font-signature:-1879047513 702020859 16 0 524289 0;}
@font-face
	{font-family:Consolas;
	panose-1:2 11 6 9 2 2 4 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:modern;
	mso-font-pitch:fixed;
	mso-font-signature:-536869121 64767 1 0 415 0;}
@font-face
	{font-family:만화진흥원체;
	panose-1:2 11 5 3 0 0 0 0 0 0;
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:variable;
	mso-font-signature:-2147482969 702020859 16 0 524289 0;}
@font-face
	{font-family:나눔바른고딕;
	mso-font-alt:"맑은 고딕";
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:variable;
	mso-font-signature:-2147482969 165117179 16 0 524289 0;}
@font-face
	{font-family:Gadugi;
	panose-1:2 11 5 2 4 2 4 2 2 3;
	mso-font-charset:0;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:-2147483645 33554432 12288 0 1 0;}
@font-face
	{font-family:"Microsoft Yi Baiti";
	panose-1:3 0 5 0 0 0 0 0 0 0;
	mso-font-charset:0;
	mso-generic-font-family:script;
	mso-font-pitch:variable;
	mso-font-signature:-2147483645 66562 524290 0 1 0;}
@font-face
	{font-family:"Segoe UI";
	panose-1:2 11 5 2 4 2 4 2 2 3;
	mso-font-charset:0;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:-469750017 -1073683329 9 0 511 0;}
@font-face
	{font-family:"Microsoft JhengHei";
	panose-1:2 11 6 4 3 5 4 4 2 4;
	mso-font-charset:136;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:679 684672000 22 0 1048585 0;}
@font-face
	{font-family:"\@맑은 고딕";
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:variable;
	mso-font-signature:-1879048145 701988091 18 0 524289 0;}
@font-face
	{font-family:"\@Microsoft JhengHei";
	mso-font-charset:136;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:679 684672000 22 0 1048585 0;}
@font-face
	{font-family:"\@굴림";
	panose-1:2 11 6 0 0 1 1 1 1 1;
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:variable;
	mso-font-signature:-1342176593 1775729915 48 0 524447 0;}
@font-face
	{font-family:"\@굴림체";
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:fixed;
	mso-font-signature:-1342176593 1775729915 48 0 524447 0;}
@font-face
	{font-family:"\@만화진흥원체";
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:variable;
	mso-font-signature:-2147482969 702020859 16 0 524289 0;}
@font-face
	{font-family:"\@나눔고딕 ExtraBold";
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:variable;
	mso-font-signature:-1879047513 702020859 16 0 524289 0;}
@font-face
	{font-family:"\@나눔바른고딕";
	mso-font-charset:129;
	mso-generic-font-family:modern;
	mso-font-pitch:variable;
	mso-font-signature:-2147482969 165117179 16 0 524289 0;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-parent:"";
	margin-top:0cm;
	margin-right:0cm;
	margin-bottom:8.0pt;
	margin-left:0cm;
	text-align:justify;
	text-justify:inter-ideograph;
	line-height:107%;
	mso-pagination:none;
	text-autospace:none;
	word-break:break-hangul;
	font-size:10.0pt;
	mso-bidi-font-size:11.0pt;
	font-family:"맑은 고딕";
	mso-ascii-font-family:"맑은 고딕";
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:"맑은 고딕";
	mso-fareast-theme-font:minor-fareast;
	mso-hansi-font-family:"맑은 고딕";
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-font-kerning:1.0pt;}
p.MsoHeader, li.MsoHeader, div.MsoHeader
	{mso-style-priority:99;
	mso-style-link:"머리글 Char";
	margin-top:0cm;
	margin-right:0cm;
	margin-bottom:8.0pt;
	margin-left:0cm;
	text-align:justify;
	text-justify:inter-ideograph;
	line-height:107%;
	mso-pagination:none;
	tab-stops:center 225.65pt right 451.3pt;
	layout-grid-mode:char;
	text-autospace:none;
	word-break:break-hangul;
	font-size:10.0pt;
	mso-bidi-font-size:11.0pt;
	font-family:"맑은 고딕";
	mso-ascii-font-family:"맑은 고딕";
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:"맑은 고딕";
	mso-fareast-theme-font:minor-fareast;
	mso-hansi-font-family:"맑은 고딕";
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-font-kerning:1.0pt;}
p.MsoFooter, li.MsoFooter, div.MsoFooter
	{mso-style-priority:99;
	mso-style-link:"바닥글 Char";
	margin-top:0cm;
	margin-right:0cm;
	margin-bottom:8.0pt;
	margin-left:0cm;
	text-align:justify;
	text-justify:inter-ideograph;
	line-height:107%;
	mso-pagination:none;
	tab-stops:center 225.65pt right 451.3pt;
	layout-grid-mode:char;
	text-autospace:none;
	word-break:break-hangul;
	font-size:10.0pt;
	mso-bidi-font-size:11.0pt;
	font-family:"맑은 고딕";
	mso-ascii-font-family:"맑은 고딕";
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:"맑은 고딕";
	mso-fareast-theme-font:minor-fareast;
	mso-hansi-font-family:"맑은 고딕";
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-font-kerning:1.0pt;}
a:link, span.MsoHyperlink
	{mso-style-priority:99;
	color:#0563C1;
	mso-themecolor:hyperlink;
	text-decoration:underline;
	text-underline:single;}
a:visited, span.MsoHyperlinkFollowed
	{mso-style-noshow:yes;
	mso-style-priority:99;
	color:#954F72;
	mso-themecolor:followedhyperlink;
	text-decoration:underline;
	text-underline:single;}
pre
	{mso-style-priority:99;
	mso-style-link:"미리 서식이 지정된 HTML Char";
	margin:0cm;
	margin-bottom:.0001pt;
	mso-pagination:widow-orphan;
	font-size:12.0pt;
	font-family:굴림체;
	mso-bidi-font-family:굴림체;}
p.MsoListParagraph, li.MsoListParagraph, div.MsoListParagraph
	{mso-style-priority:34;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	margin-top:0cm;
	margin-right:0cm;
	margin-bottom:8.0pt;
	margin-left:40.0pt;
	mso-para-margin-top:0cm;
	mso-para-margin-right:0cm;
	mso-para-margin-bottom:8.0pt;
	mso-para-margin-left:4.0gd;
	text-align:justify;
	text-justify:inter-ideograph;
	line-height:107%;
	mso-pagination:none;
	text-autospace:none;
	word-break:break-hangul;
	font-size:10.0pt;
	mso-bidi-font-size:11.0pt;
	font-family:"맑은 고딕";
	mso-ascii-font-family:"맑은 고딕";
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:"맑은 고딕";
	mso-fareast-theme-font:minor-fareast;
	mso-hansi-font-family:"맑은 고딕";
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-font-kerning:1.0pt;}
span.HTMLChar
	{mso-style-name:"미리 서식이 지정된 HTML Char";
	mso-style-priority:99;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:"미리 서식이 지정된 HTML";
	mso-ansi-font-size:12.0pt;
	mso-bidi-font-size:12.0pt;
	font-family:굴림체;
	mso-ascii-font-family:굴림체;
	mso-fareast-font-family:굴림체;
	mso-hansi-font-family:굴림체;
	mso-bidi-font-family:굴림체;
	mso-font-kerning:0pt;}
span.preprocessor
	{mso-style-name:preprocessor;
	mso-style-unhide:no;}
span.datatypes
	{mso-style-name:datatypes;
	mso-style-unhide:no;}
span.keyword
	{mso-style-name:keyword;
	mso-style-unhide:no;}
span.string
	{mso-style-name:string;
	mso-style-unhide:no;}
span.Char
	{mso-style-name:"머리글 Char";
	mso-style-priority:99;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:머리글;}
span.Char0
	{mso-style-name:"바닥글 Char";
	mso-style-priority:99;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:바닥글;}
span.tag
	{mso-style-name:tag;
	mso-style-unhide:no;}
span.tag-name
	{mso-style-name:tag-name;
	mso-style-unhide:no;}
span.attribute
	{mso-style-name:attribute;
	mso-style-unhide:no;}
span.attribute-value
	{mso-style-name:attribute-value;
	mso-style-unhide:no;}
.MsoChpDefault
	{mso-style-type:export-only;
	mso-default-props:yes;
	font-family:"맑은 고딕";
	mso-ascii-font-family:"맑은 고딕";
	mso-ascii-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;}
.MsoPapDefault
	{mso-style-type:export-only;
	margin-bottom:8.0pt;
	text-align:justify;
	text-justify:inter-ideograph;
	line-height:107%;}
 /* Page Definitions */
 @page
	{mso-page-border-surround-header:no;
	mso-page-border-surround-footer:no;
	mso-footnote-separator:url("README.files/header.htm") fs;
	mso-footnote-continuation-separator:url("README.files/header.htm") fcs;
	mso-endnote-separator:url("README.files/header.htm") es;
	mso-endnote-continuation-separator:url("README.files/header.htm") ecs;}
@page WordSection1
	{size:595.3pt 841.9pt;
	margin:3.0cm 72.0pt 72.0pt 72.0pt;
	mso-header-margin:42.55pt;
	mso-footer-margin:49.6pt;
	mso-paper-source:0;}
div.WordSection1
	{page:WordSection1;}
 /* List Definitions */
 @list l0
	{mso-list-id:46688204;
	mso-list-template-ids:2068611714;}
@list l1
	{mso-list-id:105197426;
	mso-list-template-ids:-823492142;}
@list l2
	{mso-list-id:320549872;
	mso-list-type:hybrid;
	mso-list-template-ids:946903308 1533543434 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l2:level1
	{mso-level-text:"%1\)";
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:38.0pt;
	text-indent:-18.0pt;}
@list l2:level2
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:60.0pt;
	text-indent:-20.0pt;}
@list l2:level3
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:80.0pt;
	text-indent:-20.0pt;}
@list l2:level4
	{mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:100.0pt;
	text-indent:-20.0pt;}
@list l2:level5
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:120.0pt;
	text-indent:-20.0pt;}
@list l2:level6
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:140.0pt;
	text-indent:-20.0pt;}
@list l2:level7
	{mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:160.0pt;
	text-indent:-20.0pt;}
@list l2:level8
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:180.0pt;
	text-indent:-20.0pt;}
@list l2:level9
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:200.0pt;
	text-indent:-20.0pt;}
@list l3
	{mso-list-id:356934710;
	mso-list-type:hybrid;
	mso-list-template-ids:-1389172986 -1514752746 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l3:level1
	{mso-level-text:"%1\)";
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:18.0pt;
	text-indent:-18.0pt;}
@list l3:level2
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:40.0pt;
	text-indent:-20.0pt;}
@list l3:level3
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:60.0pt;
	text-indent:-20.0pt;}
@list l3:level4
	{mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:80.0pt;
	text-indent:-20.0pt;}
@list l3:level5
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:100.0pt;
	text-indent:-20.0pt;}
@list l3:level6
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:120.0pt;
	text-indent:-20.0pt;}
@list l3:level7
	{mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:140.0pt;
	text-indent:-20.0pt;}
@list l3:level8
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:160.0pt;
	text-indent:-20.0pt;}
@list l3:level9
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:180.0pt;
	text-indent:-20.0pt;}
@list l4
	{mso-list-id:625236063;
	mso-list-template-ids:444606258;}
@list l5
	{mso-list-id:674383828;
	mso-list-template-ids:-1126671760;}
@list l6
	{mso-list-id:745878598;
	mso-list-template-ids:497565990;}
@list l7
	{mso-list-id:974412108;
	mso-list-template-ids:458007942;}
@list l8
	{mso-list-id:1456407927;
	mso-list-template-ids:-1968646960;}
@list l9
	{mso-list-id:1537545542;
	mso-list-template-ids:-2091760642;}
@list l10
	{mso-list-id:1539388447;
	mso-list-template-ids:1905804902;}
@list l11
	{mso-list-id:1581258259;
	mso-list-type:hybrid;
	mso-list-template-ids:-492793102 1535015832 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l11:level1
	{mso-level-text:"%1\)";
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:38.0pt;
	text-indent:-18.0pt;}
@list l11:level2
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:60.0pt;
	text-indent:-20.0pt;}
@list l11:level3
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:80.0pt;
	text-indent:-20.0pt;}
@list l11:level4
	{mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:100.0pt;
	text-indent:-20.0pt;}
@list l11:level5
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:120.0pt;
	text-indent:-20.0pt;}
@list l11:level6
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:140.0pt;
	text-indent:-20.0pt;}
@list l11:level7
	{mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:160.0pt;
	text-indent:-20.0pt;}
@list l11:level8
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:180.0pt;
	text-indent:-20.0pt;}
@list l11:level9
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:200.0pt;
	text-indent:-20.0pt;}
@list l12
	{mso-list-id:1807508218;
	mso-list-template-ids:-643952582;}
@list l13
	{mso-list-id:1880779413;
	mso-list-type:hybrid;
	mso-list-template-ids:-760193296 -748496430 67698713 67698715 67698703 67698713 67698715 67698703 67698713 67698715;}
@list l13:level1
	{mso-level-text:"%1\)";
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:38.0pt;
	text-indent:-18.0pt;}
@list l13:level2
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:60.0pt;
	text-indent:-20.0pt;}
@list l13:level3
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:80.0pt;
	text-indent:-20.0pt;}
@list l13:level4
	{mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:100.0pt;
	text-indent:-20.0pt;}
@list l13:level5
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:120.0pt;
	text-indent:-20.0pt;}
@list l13:level6
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:140.0pt;
	text-indent:-20.0pt;}
@list l13:level7
	{mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:160.0pt;
	text-indent:-20.0pt;}
@list l13:level8
	{mso-level-number-format:alpha-upper;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:180.0pt;
	text-indent:-20.0pt;}
@list l13:level9
	{mso-level-number-format:roman-lower;
	mso-level-tab-stop:none;
	mso-level-number-position:right;
	margin-left:200.0pt;
	text-indent:-20.0pt;}
@list l14
	{mso-list-id:1942102122;
	mso-list-template-ids:1389924410;}
@list l15
	{mso-list-id:1989896209;
	mso-list-template-ids:1626903156;}
@list l16
	{mso-list-id:2091005711;
	mso-list-template-ids:-544048824;}
@list l17
	{mso-list-id:2138331872;
	mso-list-template-ids:-25102342;}
ol
	{margin-bottom:0cm;}
ul
	{margin-bottom:0cm;}
-->
</style>
<!--[if gte mso 10]>
<style>
 /* Style Definitions */
 table.MsoNormalTable
	{mso-style-name:"표준 표";
	mso-tstyle-rowband-size:0;
	mso-tstyle-colband-size:0;
	mso-style-noshow:yes;
	mso-style-priority:99;
	mso-style-parent:"";
	mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
	mso-para-margin-top:0cm;
	mso-para-margin-right:0cm;
	mso-para-margin-bottom:8.0pt;
	mso-para-margin-left:0cm;
	text-align:justify;
	text-justify:inter-ideograph;
	line-height:107%;
	mso-pagination:widow-orphan;
	font-size:10.0pt;
	mso-bidi-font-size:11.0pt;
	font-family:"맑은 고딕";
	mso-ascii-font-family:"맑은 고딕";
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:"맑은 고딕";
	mso-fareast-theme-font:minor-fareast;
	mso-hansi-font-family:"맑은 고딕";
	mso-hansi-theme-font:minor-latin;
	mso-font-kerning:1.0pt;}
</style>
<![endif]--><!--[if gte mso 9]><xml>
 <o:shapedefaults v:ext="edit" spidmax="2049"/>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <o:shapelayout v:ext="edit">
  <o:idmap v:ext="edit" data="1"/>
 </o:shapelayout></xml><![endif]-->
</head>

<body lang=KO link="#0563C1" vlink="#954F72" style='tab-interval:40.0pt'>

<div class=WordSection1>

<p class=MsoNormal style='line-height:normal'><span lang=EN-US
style='font-size:14.0pt;mso-bidi-font-size:12.0pt;font-family:"나눔고딕 ExtraBold"'>ROOTCTF
</span><span style='font-size:14.0pt;mso-bidi-font-size:12.0pt;font-family:
"나눔고딕 ExtraBold"'>제<span lang=EN-US> 1</span>회 서울디지텍고등학교 청소년 해킹방어대회<span
lang=EN-US> Write-Up <o:p></o:p></span></span></p>

<p class=MsoNormal align=right style='text-align:right;line-height:normal'><span
lang=EN-US style='font-size:14.0pt;mso-bidi-font-size:12.0pt;font-family:"나눔고딕 ExtraBold";
mso-no-proof:yes'>JunhoYeo(</span><span style='font-size:14.0pt;mso-bidi-font-size:
12.0pt;font-family:"나눔고딕 ExtraBold";mso-no-proof:yes'>여준호<span lang=EN-US>)
10st / 3147p<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:14.0pt;font-family:"나눔고딕 ExtraBold";mso-no-proof:
yes'>MISC &#8211; Welcome(50)<o:p></o:p></span></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l0 level1 lfo2;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>제</span><span lang=EN-US style='font-size:
9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>&nbsp;1</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>회</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>서울디지텍고등학교</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>해킹방어대회</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l0 level1 lfo2;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>에</span><span lang=EN-US style='font-size:
9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>오신</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>것을</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>환영합니다</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l0 level1 lfo2;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>3.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>모든</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>문제의</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>정답은</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>다음과</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>같은</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>형식을</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>가지고</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>있습니다</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l0 level1 lfo2;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>4.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>정답</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>형식</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;=&nbsp;FLAG{</span><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>내용</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>}&nbsp;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l0 level1 lfo2;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>5.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l0 level1 lfo2;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>6.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>FLAG{Welcome_to_Seoul_Digitech_ROOT_CTF}&nbsp;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;font-family:만화진흥원체;mso-no-proof:yes'>정답 형식을 알려주는 문제로<span
lang=EN-US>, </span>그대로 문제에 나온 대로 입력하면 된다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;font-family:만화진흥원체;background:lightgrey;
mso-highlight:lightgrey;mso-no-proof:yes'>FLAG{Welcome_to_Seoul_Digitech_ROOT_CTF}</span><span
lang=EN-US style='font-size:11.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:5.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><span
style='mso-spacerun:yes'>&nbsp;</span><span
style='mso-spacerun:yes'>&nbsp;</span><o:p></o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:14.0pt;font-family:"나눔고딕 ExtraBold";mso-no-proof:
yes'>MISC &#8211; Find The Flag(913)<o:p></o:p></span></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l5 level1 lfo3;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>문제</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>출제자는</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>크리스마스에</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>혼자</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>보내야</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>된다는</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>생각에</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>화가</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>나서</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>플래그를</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>숨겨버렸습니다</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>.&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#5C5C5C;
mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l5 level1 lfo3;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>문제</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>출제자가</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>숨긴</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>플래그를</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>찾아주세요</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>!&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#5C5C5C;
mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l5 level1 lfo3;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>3.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>HINT:JS&nbsp;file,WebCacheV01.dat&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>분석</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#5C5C5C;
mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>다른 문제들을 보면 알겠지만<span lang=EN-US>, </span>해당 <span lang=EN-US>CTF</span>에서는
구글 드라이브를 통해 파일을 공유한다<span lang=EN-US>. </span>그렇기 때문에 <span lang=EN-US>JS file</span>을
다운로드 받을 수 있는 구글 드라이브 공유 링크가 <span lang=EN-US>WebCacheV01.dat</span>에 있을 것이라고 생각했다<span
lang=EN-US>. <o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><v:shapetype id="_x0000_t75" coordsize="21600,21600" o:spt="75"
 o:preferrelative="t" path="m@4@5l@4@11@9@11@9@5xe" filled="f" stroked="f">
 <v:stroke joinstyle="miter"/>
 <v:formulas>
  <v:f eqn="if lineDrawn pixelLineWidth 0"/>
  <v:f eqn="sum @0 1 0"/>
  <v:f eqn="sum 0 0 @1"/>
  <v:f eqn="prod @2 1 2"/>
  <v:f eqn="prod @3 21600 pixelWidth"/>
  <v:f eqn="prod @3 21600 pixelHeight"/>
  <v:f eqn="sum @0 0 1"/>
  <v:f eqn="prod @6 1 2"/>
  <v:f eqn="prod @7 21600 pixelWidth"/>
  <v:f eqn="sum @8 21600 0"/>
  <v:f eqn="prod @7 21600 pixelHeight"/>
  <v:f eqn="sum @10 21600 0"/>
 </v:formulas>
 <v:path o:extrusionok="f" gradientshapeok="t" o:connecttype="rect"/>
 <o:lock v:ext="edit" aspectratio="t"/>
</v:shapetype><v:shape id="그림_x0020_12" o:spid="_x0000_i1061" type="#_x0000_t75"
 style='width:451.5pt;height:254.25pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image001.png" o:title=""/>
</v:shape><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>먼저 리눅스 터미널의 <span lang=EN-US>strings </span>명령어를 사용하여 <span
lang=EN-US>WebCacheV01.dat</span>에서 문자열 데이터만을 뽑아내어 파일에 저장해 두었다<span lang=EN-US>.
</span>그리고 검색 기능을 사용하여 구글 드라이브 공유 링크를 찾아냈다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><v:shape id="그림_x0020_13" o:spid="_x0000_i1060" type="#_x0000_t75"
 style='width:451.5pt;height:254.25pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image002.png" o:title=""/>
</v:shape><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>해당 링크에서<span lang=EN-US> YWRtaW5fcm9vdA.js </span>파일을 다운로드할 수
있었다<span lang=EN-US>. </span>그러나 도저히 <span lang=EN-US>JavaScript file</span>로는 보이지
않았다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><v:shape id="그림_x0020_14" o:spid="_x0000_i1059" type="#_x0000_t75"
 style='width:451.5pt;height:254.25pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image003.png" o:title=""/>
</v:shape><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>파일의 <span lang=EN-US>hex code</span>를 보니 <span lang=EN-US>header
signature</span>가 <span lang=EN-US>PNG file</span>로 되어 있어서<span lang=EN-US>, </span>확장자를
<span lang=EN-US>.PNG</span>로 변경한 뒤 열어보았더니 플래그가 아니라고 떴다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><v:shape id="그림_x0020_15" o:spid="_x0000_i1058" type="#_x0000_t75"
 style='width:451.5pt;height:254.25pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image004.png" o:title=""/>
</v:shape><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>다행히 <span lang=EN-US>hex code </span>중간에서 플래그를 찾을 수 있었다<span
lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><v:shape id="그림_x0020_16" o:spid="_x0000_i1057" type="#_x0000_t75"
 style='width:451.5pt;height:254.25pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image005.png" o:title=""/>
</v:shape><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>여담이지만 그냥 다운받아서 <span lang=EN-US>hexdump </span>뜰 필요 없이 처음부터 플래그가
있었다<span lang=EN-US>… </span>씁쓸<span lang=EN-US><span
style='mso-spacerun:yes'>&nbsp; </span><o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
background:lightgrey;mso-highlight:lightgrey;mso-no-proof:yes'>FLAG{I3_Br0wser_F0r3ns1c_4ND_RoUgh_W0rk}</span><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'>MISC &#8211; Calculate(167)<o:p></o:p></span></b></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l8 level1 lfo4;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>누가</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>내</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>패스워드좀</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>알려줘</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>!&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l8 level1 lfo4;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>hint&nbsp;:&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>역연산</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#5C5C5C;
mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_17" o:spid="_x0000_i1056"
 type="#_x0000_t75" style='width:450.75pt;height:228pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image006.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>주어진 링크에 들어가니 <span lang=EN-US>Python</span>으로 작성된 소스코드를 확인할 수
있었다<span lang=EN-US>. <o:p></o:p></span></span></p>

<pre style='background:white'><span lang=EN-US style='font-size:11.0pt;
mso-bidi-font-size:14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>jdoodle.com/python-programming-online</span><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>에서 코드를 실행하니 사용자에게 문자열을 입력받아 암호화 함수인 <span lang=EN-US>one(), two(), three(), four()</span>를 순서대로 호출하여 문자열의 문자를 하나씩 암호화한 뒤 플래그값이 암호화되어 저장된 것으로 추정되는 <span
lang=EN-US>result </span>배열의 값과 비교하여 일치하면 <span lang=EN-US>‘Correct!!’, </span>일치하지 않으면 <span
lang=EN-US>‘Incorrect..’</span>를 출력하는 것 같았다<span lang=EN-US>.<o:p></o:p></span></span></pre>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:gray;mso-font-kerning:0pt'>#include&nbsp;&lt;stdio.h&gt;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><b><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:seagreen;mso-font-kerning:0pt'>int</span></b><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;one(</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;num,&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;size){&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>3.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;r&nbsp;=&nbsp;num&nbsp;+&nbsp;size;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>4.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;r&nbsp;+=&nbsp;915;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>5.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>return</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;r;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>6.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>}&nbsp;&nbsp;</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>7.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><b><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:seagreen;mso-font-kerning:0pt'>int</span></b><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;two(</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;num,&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;size){&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>8.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;r&nbsp;=&nbsp;num&nbsp;-&nbsp;size;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>9.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;r&nbsp;-=&nbsp;372;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>10.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>return</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;r;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>11.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>}&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>12.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;three(</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;num,&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;size){&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>13.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;r&nbsp;=&nbsp;num&nbsp;^&nbsp;size;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>14.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;r&nbsp;^=&nbsp;826;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>15.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>return</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;r;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>16.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>}&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>17.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;four(</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;num,&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;size){&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>18.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;size&nbsp;%=&nbsp;32;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>19.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;r&nbsp;=&nbsp;num&nbsp;&gt;&gt;&nbsp;(32&nbsp;-&nbsp;size);&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>20.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;b&nbsp;=&nbsp;(num&nbsp;&lt;&lt;&nbsp;size)&nbsp;-&nbsp;(r&nbsp;&lt;&lt;&nbsp;32);&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>21.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>return</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;b&nbsp;+&nbsp;r;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>22.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>}&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>23.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;main(){&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>24.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;result[32]&nbsp;=&nbsp;{5040,&nbsp;4944,&nbsp;5088,&nbsp;4992,&nbsp;7232,&nbsp;4848,&nbsp;7584,&nbsp;7344,&nbsp;4288,&nbsp;7408,&nbsp;7360,&nbsp;7584,&nbsp;4608,&nbsp;4880,&nbsp;4320,&nbsp;7328,&nbsp;7360,&nbsp;4608,&nbsp;4896,&nbsp;4320,&nbsp;7472,&nbsp;7328,&nbsp;7360,&nbsp;4608,&nbsp;4752,&nbsp;4368,&nbsp;4848,&nbsp;4608,&nbsp;4848,&nbsp;4368,&nbsp;4944,&nbsp;7200};&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>25.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>char</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;data[100]=</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;qwertyuiop{}asdfghjkl!?zxcvbnm,.QWERTYUIOPASDFGHJKLZXCVBNM_1234567890&quot;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>26.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>for</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>(</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;i=0;&nbsp;i&lt;32;&nbsp;i++){&nbsp;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>27.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>for</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>(</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;j=0;&nbsp;j&lt;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>sizeof</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>(data);&nbsp;j++){&nbsp;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>28.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;number;&nbsp;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>29.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:seagreen;mso-font-kerning:0pt'>int</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;str=data[j];&nbsp;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>30.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number=one(str,100);&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>31.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number=two(number,100);&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>32.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number=three(number,100);&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>33.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number=four(number,100);&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>34.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>(result[i]==number){&nbsp;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>35.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;printf(</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;%c&quot;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>,&nbsp;data[j]);&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>36.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>break</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>;&nbsp;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>37.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>38.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>39.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>40.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>return</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;0;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l4 level1 lfo1;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>41.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>}&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<pre style='background:white'><span style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>노가다 스피릿으로 하나씩 직접 입력해 코드표를 만드려는 생각도 들었지만 순간 이건 아니라는 것을 깨닫고 위와 같이<span
lang=EN-US> C</span>언어로 <span lang=EN-US>Flag</span>값을 출력하는 소스코드를 작성했다<span
lang=EN-US>. <o:p></o:p></span></span></pre><pre style='background:white'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>파이썬도 좋겠지만 <span lang=EN-US>C</span>언어로 하면 더 재미있을 것 같았기 때문에 <span
lang=EN-US><o:p></o:p></span></span></pre><pre style='background:white'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>-</span><span style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>라고 쓰고 파이썬을 못해서 그랬다고 읽으면 될 것이다<span
lang=EN-US>… </span>씨익<span lang=EN-US><o:p></o:p></span></span></pre><pre
style='background:white'><span style='font-size:11.0pt;mso-bidi-font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'>배열 <span lang=EN-US>result</span>에는<span
lang=EN-US> Flag</span>가 암호화된 값이<span lang=EN-US>, </span>배열<span lang=EN-US> data</span>에는 <span
lang=EN-US>Flag</span>를 이룰 것으로 추정되는 문자들이 저장되어 있다<span lang=EN-US>. </span>배열 <span
lang=EN-US>result</span>에서 알 수 있듯이 <span lang=EN-US>Flag</span>는 총<span
lang=EN-US> 32</span>개의 문자로 구성되어 있다<span lang=EN-US>.<o:p></o:p></span></span></pre><pre
style='background:white'><span style='font-size:11.0pt;mso-bidi-font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'>이중<span lang=EN-US> for</span>문을 사용하여 <span
lang=EN-US>result[i]</span>의 값과<span lang=EN-US> data[j]</span>를 암호화 함수를 순서대로 암호화한 값 <span
lang=EN-US>number</span>를 비교해 두 값이 일치하면 해당 <span lang=EN-US>data[j]</span>를 출력하고<span
lang=EN-US> break</span>하여 배열 <span lang=EN-US>result</span>의 다음 값을 구하고<span
lang=EN-US>, </span>일치하지 않으면 배열 <span lang=EN-US>data</span>의 다음 값과 비교하는 구조로 플래그를 출력한다<span
lang=EN-US>.<o:p></o:p></span></span></pre><pre style='background:white'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>간단한 코드니까 금방 이해할 수 있을 거라고 생각한다<span lang=EN-US>. <o:p></o:p></span></span></pre><pre
style='background:white'><span lang=EN-US style='mso-no-proof:yes'><v:shape
 id="그림_x0020_19" o:spid="_x0000_i1055" type="#_x0000_t75" style='width:343.5pt;
 height:82.5pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image007.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></pre><pre
style='background:white'><span style='font-size:11.0pt;mso-bidi-font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'>프로그램을 실행하면 위처럼 <span lang=EN-US>Flag</span>가 나온다<span
lang=EN-US>. <o:p></o:p></span></span></pre><pre style='background:white'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>여담으로 다른 분들께서는 역연산 함수를 만들어서 푸신 분들이 많은 것 같다<span lang=EN-US>.<o:p></o:p></span></span></pre><pre
style='background:white'><span style='font-size:11.0pt;mso-bidi-font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'>그런데 개인적으로는 저렇게 하나씩 암호화해서 비교하는 브루트 포싱으로 푸는 것도 재미있고 더 빨리 짤 수 있는 것 같다<span
lang=EN-US>. </span>이는 역시 역연산 함수를 만드는 것을 못해서 그랬다고 읽으면 될 것 같다<span lang=EN-US>.<o:p></o:p></span></span></pre>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
background:lightgrey;mso-highlight:lightgrey;mso-no-proof:yes'>FLAG{Rev3rse_P1us_M1nus_X0R_R0L}</span><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'>MISC &#8211; Vocabulary<o:p></o:p></span></b></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l16 level1 lfo5;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>플래그가</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>적힌</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>친구의</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>단어장을</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>잃어버렸다</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l16 level1 lfo5;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>어서</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>빨리</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>찾아야</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>된다</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>.&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l16 level1 lfo5;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>3.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>그</span><span lang=EN-US style='font-size:
9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>친구가</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>화내기</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>전에</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>플래그라도</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>찾아보자</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#5C5C5C;
mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l16 level1 lfo5;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>4.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>hint&nbsp;:&nbsp;PNG&nbsp;height&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'><v:shape
 id="그림_x0020_3" o:spid="_x0000_i1054" type="#_x0000_t75" style='width:250.5pt;
 height:268.5pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image008.png" o:title=""/>
</v:shape><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>pleas_find.png
</span><span style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>파일을 다운로드하여
확인하고 청개구리처럼 <span lang=EN-US>hex editor</span>로 열어봤는데 보기 불편해서 그냥 열라는 대로 <span
lang=EN-US>notepad</span>로 열어봤다<span lang=EN-US>. <o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_5" o:spid="_x0000_i1053"
 type="#_x0000_t75" style='width:282.75pt;height:262.5pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image009.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;
mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>파일 끝부분에 단어장이 보인다<span
lang=EN-US>. </span>영국에서 시작된 어디서 많이 본 듯한 편지와 <span lang=EN-US>Fake Flag, </span>그리고
<span lang=EN-US>height</span>를 <span lang=EN-US>1000px</span>로 <span
lang=EN-US>increase</span>하라는 힌트가 나왔다<span lang=EN-US>. </span>그래서 그림판을 사용해서 급한대로
옮겼더니 이미지가 깨져버렸다<span lang=EN-US>. <o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>그렇다면 혹시 <span
lang=EN-US>hex edit</span>을 하여 <span lang=EN-US>PNG file</span>의 <span
lang=EN-US>height</span>를 고치라는 게 아닐까<span lang=EN-US>?<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>물론 그걸 어떻게 할지 모르기 때문에<span
lang=EN-US>! </span>구글링을 하여 자료를 찾아보았다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>https://www.linkedin.com/pulse/hex-editing-width-height-png-files-ciaran-mc-ardle<o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>PNG hex
edit</span><span style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>을
하여 이미지의 <span lang=EN-US>width, height data</span>를 바꾸는 것에 관한 링크다<span
lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'><v:shape
 id="그림_x0020_30" o:spid="_x0000_i1052" type="#_x0000_t75" style='width:451.5pt;
 height:96pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image010.png" o:title=""/>
</v:shape><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>저기에 표시한 파란 부분을 수정하면
<span lang=EN-US>PNG width, </span>빨간 부분을 수정하면 <span lang=EN-US>PNG height</span>를
고칠 수 있는 것 같다<span lang=EN-US>. <o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'><v:shape
 id="그림_x0020_31" o:spid="_x0000_i1051" type="#_x0000_t75" style='width:323.25pt;
 height:96pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image011.png" o:title=""/>
</v:shape><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>1000px</span><span
style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>로 바꾸라고 하였으므로 <span
lang=EN-US>02 EE</span>를 <span lang=EN-US>1000</span>의 <span lang=EN-US>16</span>진수
값인 <span lang=EN-US>03 E8</span>로 고쳤다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'><v:shape
 id="그림_x0020_32" o:spid="_x0000_i1050" type="#_x0000_t75" style='width:160.5pt;
 height:228.75pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image012.png" o:title=""/>
</v:shape><v:shape id="그림_x0020_33" o:spid="_x0000_i1049" type="#_x0000_t75"
 style='width:267pt;height:187.5pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image013.png" o:title=""/>
</v:shape><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>저 밑에 <span
lang=EN-US>‘Hello :) Go Down! </span></span><span style='font-size:11.0pt;
mso-ascii-font-family:"맑은 고딕";mso-fareast-font-family:"맑은 고딕";mso-hansi-font-family:
"맑은 고딕";mso-no-proof:yes'>↓</span><span lang=EN-US style='font-size:11.0pt;
font-family:나눔바른고딕;mso-no-proof:yes'>’ </span><span style='font-size:11.0pt;
font-family:나눔바른고딕;mso-no-proof:yes'>부분이 나타났다<span lang=EN-US>. </span>더 내려가면 플래그가
있는 듯하다<span lang=EN-US>. </span>그냥 두 배<span lang=EN-US>, 2000px</span>으로 길이를 바꿔보기로
했다<span lang=EN-US>. 2000</span>의 <span lang=EN-US>16</span>진수 값인 <span
lang=EN-US>07 D0</span>으로 고쳤다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_36" o:spid="_x0000_i1048"
 type="#_x0000_t75" style='width:451.5pt;height:254.25pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image014.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;
mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>어라라<span
lang=EN-US>! </span>뭔가가 보인다<span lang=EN-US>. <o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_37" o:spid="_x0000_i1047"
 type="#_x0000_t75" style='width:451.5pt;height:254.25pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image015.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;
mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'>플래그가 나타났다<span
lang=EN-US>!<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;background:lightgrey;
mso-highlight:lightgrey;mso-no-proof:yes'>FLAG{_1vErticAl_2rEADiNg_3TAStlSb}</span><span
lang=EN-US style='font-size:11.0pt;font-family:나눔바른고딕;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'>REVERSING &#8211; Stage Game(229)<o:p></o:p></span></b></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l6 level1 lfo6;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>인내의</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>시간</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>..&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#5C5C5C;
mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l6 level1 lfo6;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>Stage&nbsp;Level&nbsp;1~10&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l6 level1 lfo6;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>3.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>hint&nbsp;:&nbsp;Sleep&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_23" o:spid="_x0000_i1046"
 type="#_x0000_t75" style='width:451.5pt;height:249pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image016.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_38" o:spid="_x0000_i1045"
 type="#_x0000_t75" style='width:450.75pt;height:235.5pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image017.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>Stage.exe </span><span style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>파일이 주어진다<span lang=EN-US>. </span>실행해
본 결과 다음과 같은 프로그램인 것 같다<span lang=EN-US>. </span>먼저 실행되면 기다릴 수 있는지를 물어보고 <span
lang=EN-US>1</span>이면 스테이지 게임 시작<span lang=EN-US>, 0</span>이면 종료를 한다<span
lang=EN-US>. </span>게임 내용은 그냥 <span lang=EN-US>sleep() </span>함수 등으로 일정한 시간 동안 기다리게
하다가 다음 스테이지로 넘어가고 거기서 더 기다리면 다음 스테이지로 넘어가고 하는 것을 반복하면 플래그를 주고 끝나는 것 같다<span
lang=EN-US>. </span>문제는 기다리는 시간이 너무 길다는 것이다<span lang=EN-US>. </span>본인의 인내심으로는
<span lang=EN-US>3</span>번 스테이지가 한계인 것 같다<span lang=EN-US>… </span>리버싱해서 수정해 보자<span
lang=EN-US>!<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_20" o:spid="_x0000_i1044"
 type="#_x0000_t75" style='width:418.5pt;height:356.25pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image018.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>올리디버거로 열고 <span lang=EN-US>All referenced text strings</span>으로
문자열만 모아서 확인해보니 저렇게 문자열들이 나온다<span lang=EN-US>. </span><s>아이 기분좋아</s><span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_21" o:spid="_x0000_i1043"
 type="#_x0000_t75" style='width:366.75pt;height:221.25pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image019.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>저 중 하나를 클릭해 보면 역시<span lang=EN-US>! </span>예상대로 <span
lang=EN-US>Sleep() </span>함수를 호출<span lang=EN-US>(call)</span>하여 <span
lang=EN-US>delay</span>를 발생시킨다는 것을 볼 수 있다<span lang=EN-US>. </span>이걸 <span
lang=EN-US>‘</span>아무것도 안 하는<span lang=EN-US>’ </span>어셈블리 명령으로 바꾸면 될 것 같은데<span
lang=EN-US>…<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_22" o:spid="_x0000_i1042"
 type="#_x0000_t75" style='width:329.25pt;height:223.5pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image020.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>바로 <span lang=EN-US>NOP(No OPeration) </span>명령을 쓰면 될 것 같다<span
lang=EN-US>. </span>어셈블리에서 아무 것도 안 하고 넘어가는 명령이다<span lang=EN-US>. </span>버퍼 오버플로우<span
lang=EN-US>(BOF) </span>공격에서 <span lang=EN-US>NOP sled</span>를 만들 때 사용하는 바로 그 명령<span
lang=EN-US>!<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>저기 <span lang=EN-US>PUSH EAX </span>명령은 왠지 <span lang=EN-US>Sleep()
</span>함수에 전달되는 인수인 것 같아서 그냥 <span lang=EN-US>CALL </span>명령이랑 같이<span
lang=EN-US> NOP</span>처리를 했는데 왠지 안 했어도 됬을 것 같은 기분이 든다<span lang=EN-US>. </span>뭐
하는 명령인지도 궁금하다<span lang=EN-US>. <o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_24" o:spid="_x0000_i1041"
 type="#_x0000_t75" style='width:351.75pt;height:73.5pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image021.png" o:title=""
  cropbottom="2783f"/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>All intermodular calls</span><span style='font-size:11.0pt;
mso-bidi-font-size:14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>로 사용한 <span
lang=EN-US>API </span>함수들을 모아 볼 수 있다<span lang=EN-US>. </span>이걸 참고해서 다음으로 패치해야
하는 부분을 볼 수 있다<span lang=EN-US>. </span>또 마지막에 <span lang=EN-US>JMP</span>로 <span
lang=EN-US>Sleep() </span>함수로 넘어가는<span lang=EN-US>? </span>부분이 있던 것 같은데 그 부분도 패치해줘야
한다<span lang=EN-US>. </span>왜 그런지는 모르겠는데 아마 마지막 스테이지를 통과하고도 좀 더 기다려야 플래그가 나오는 게
아닐까<span lang=EN-US>? </span>리버싱 까막눈이라 모르겠지만 언젠가 똭<span lang=EN-US>! </span>보면 똭<span
lang=EN-US>! </span>이해할 날이 오겠지<span lang=EN-US>… <o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><v:shape id="그림_x0020_40" o:spid="_x0000_i1040" type="#_x0000_t75"
 style='width:250.5pt;height:97.5pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image022.png" o:title=""
  cropbottom="50659f" cropleft="100f" cropright="45352f"/>
</v:shape><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>저렇게 다 <span lang=EN-US>NOP</span>로 패치한 프로그램을 실행하니 플래그가 나왔다<span
lang=EN-US>. CTF</span>에서 내가 처음으로 푼 리버싱 문제라서 그런지 정말 기분이 좋았다<span lang=EN-US>. </span>어떤
문서에서 쉘이 따지고 플래그가 나왔을 때의 쾌감이 있다는데 이런 게 바로 그런 것일까<span lang=EN-US>… </span>흐헿헿<span
lang=EN-US>(?) <s>+)</s></span><s>여기서는 처음이자 마지막 리버싱 문제였다칸다ㅠ</s><span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
background:lightgrey;mso-highlight:lightgrey;mso-no-proof:yes'>FLAG{Y0ur_p4t1enc3_1s_gr3at}</span><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'>WEBHACKING &#8211; Login<o:p></o:p></span></b></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l1 level1 lfo7;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>로그인</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>페이지인데</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>로그인이</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>안된다</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>...&nbsp;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l1 level1 lfo7;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>로그인을</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>성공하고</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>짱해커가</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>되어보자</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>!!&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l1 level1 lfo7;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>3.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>Hint&nbsp;:&nbsp;Array,&nbsp;length&lt;6&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l1 level1 lfo7;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>4.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>Hint2&nbsp;:&nbsp;Get</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>으로</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>배열을</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>전송하는</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>방법</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>,&nbsp;sql&nbsp;injection&nbsp;&nbsp;</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>진짜 오랫동안 헤맷지만 답은 꽤 가까이에 있었던 문제<span lang=EN-US>…<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_41" o:spid="_x0000_i1039"
 type="#_x0000_t75" style='width:201.75pt;height:124.5pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image023.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>페이지에 들어가면<span lang=EN-US> go! </span>버튼이 나오는데<span
lang=EN-US>, </span>이를 누르면 <span lang=EN-US>login.php</span>으로 <span
lang=EN-US>pw=guest</span>라는 값을 전달하며 리디렉션해준다<span lang=EN-US>. <o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_42" o:spid="_x0000_i1038"
 type="#_x0000_t75" style='width:451.5pt;height:159.75pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image024.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>login.php</span><span style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>에 가면 위와 같은 <span lang=EN-US>PHP </span>소스코드를
볼 수 있다<span lang=EN-US>. _GET() </span>함수로 <span lang=EN-US>pw, fpw </span>변수의 값을
받아와서 <span lang=EN-US>SQL </span>어쩌고 저쩌고 해서 받아온<span lang=EN-US> result </span>배열의
<span lang=EN-US>id</span>값이 <span lang=EN-US>True</span>면<span lang=EN-US>(?)
flag</span>라는 쿠키를 생성하고 저 값을 집어넣은 뒤 <span lang=EN-US>flag.html</span>로 리디렉션 하는 것
같다<span lang=EN-US>. </span>그러면 <span lang=EN-US>flag.html</span>에 <span
lang=EN-US>Flag</span>값이 나오겠지<span lang=EN-US>?<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>뭐 딱 봐도 <span lang=EN-US>SQL Injection(SQLI) </span>공격을 해야 하는 것
같다<span lang=EN-US>. </span>물론 본인은 <span lang=EN-US>SQL </span>지식이 전혀 없으므로 먼저 꼼수를
시도해봤다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='margin-left:10.0pt;mso-para-margin-left:
1.0gd;text-align:left;line-height:normal'><span lang=EN-US style='font-size:
11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>1) </span><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>그냥<span lang=EN-US> flag.html</span>로 고고싱<span lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='margin-left:10.0pt;mso-para-margin-left:
1.0gd;text-align:left;line-height:normal'><span lang=EN-US style='mso-no-proof:
yes'><v:shape id="그림_x0020_43" o:spid="_x0000_i1037" type="#_x0000_t75"
 style='width:195pt;height:66pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image025.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><span
style='mso-spacerun:yes'>&nbsp;</span></span><span style='font-size:11.0pt;
mso-bidi-font-size:14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>실패다<span
lang=EN-US>!<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='margin-left:10.0pt;mso-para-margin-left:
1.0gd;text-align:left;line-height:normal'><span lang=EN-US style='font-size:
11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>2) </span><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>쿠키 값을 변조 후<span lang=EN-US> flag.html</span>로 고고싱 <span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='margin-left:10.0pt;mso-para-margin-left:
1.0gd;text-align:left;line-height:normal'><span lang=EN-US style='mso-no-proof:
yes'><v:shape id="그림_x0020_44" o:spid="_x0000_i1036" type="#_x0000_t75"
 style='width:246pt;height:132pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image026.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-left:10.0pt;mso-para-margin-left:
1.0gd;text-align:left;line-height:normal'><span lang=EN-US style='font-size:
11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>EditThisCookie</span><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>라는 <span lang=EN-US>chrome extension</span>을 사용해서 위와 같이 쿠키를 만들었다<span
lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='margin-left:10.0pt;mso-para-margin-left:
1.0gd;text-align:left;line-height:normal'><span style='font-size:11.0pt;
mso-bidi-font-size:14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>역시 <span
lang=EN-US>FLAG IS IN HERE</span>만 나올 뿐<span lang=EN-US>… </span>실패닷<span
lang=EN-US>!<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>결국<span lang=EN-US> SQL injection </span>뿐인가<span lang=EN-US>…
</span>여러가지 방법들을 사용해 봤지만 리디렉션은 되지 않았다<span lang=EN-US>..<o:p></o:p></span></span></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l7 level1 lfo12;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>http://sdhsroot.kro.kr/Login/login.php?<span
style='background:yellow;mso-highlight:yellow'>pw[1]=</span></span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;background:yellow;mso-highlight:yellow;
mso-font-kerning:0pt'>'OR'</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;background:yellow;mso-highlight:yellow;mso-font-kerning:0pt'>1</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>끈질긴 구글링 끝에 <span lang=EN-US>_GET()</span>으로 <span lang=EN-US>array</span>를
전달하는 방법을 겨우겨우 알아내 위처럼 <span lang=EN-US>SQL </span>인젝션을 시도했다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_47" o:spid="_x0000_i1035"
 type="#_x0000_t75" style='width:192pt;height:64.5pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image027.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>Flag </span><span style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>쿠키가 생성되고 리디렉션은 되었지만<span
lang=EN-US>… </span>플래그는 나오지 않았다<span lang=EN-US>. </span>페이지 소스보기를 해도 나오지 않는 시츄레이션이라
멘붕이 제대로 왔다<span lang=EN-US>. <o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>설마 <span lang=EN-US>Flag </span>쿠키에 저장되는 값이 플래그일까<span
lang=EN-US>? Base64 format</span>으로 <span lang=EN-US>decode</span>를 시도해 보자 다시 <span
lang=EN-US>Base64</span>로 <span lang=EN-US>encode</span>된 값이 나오길래 아래처럼 플래그가 나올 때까지
계속 <span lang=EN-US>decode</span>하며 해결했다<span lang=EN-US>.</span></span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'> <o:p></o:p></span></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l14 level1 lfo14;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>VmxjeE1FNUdSbk5UV0hCclUwVmFiMWxzVm1GTlZtUnhVbFJXYVZKdGVGcFdSM0JYWWxaV1ZVMUVhejA9&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l14 level1 lfo14;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>VlcxME5GRnNTWHBrU0Vab1lsVmFNVmRxUlRWaVJteFpWR3BXYlZWVU1Eaz0=&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l14 level1 lfo14;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>3.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>VW10NFFsSXpkSEZoYlVaMVdqRTViRmxZVGpWbVVUMDk=&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l14 level1 lfo14;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>4.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>Umt4QlIzdHFhbUZ1WjE5bFlYTjVmUT09&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l14 level1 lfo14;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>5.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>RkxBR3tqamFuZ19lYXN5fQ==&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l14 level1 lfo14;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>6.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>FLAG{jjang_easy}&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
background:lightgrey;mso-highlight:lightgrey;mso-no-proof:yes'>FLAG{jjang_easy}</span><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'>WEBHACKING &#8211; SPACE PROSPECTION<o:p></o:p></span></b></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l12 level1 lfo15;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>2023</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>년</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>...&nbsp;SPACE&nbsp;PROSPECTION</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>라는</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>회사가</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>화성에</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>진출했다</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>.&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#5C5C5C;
mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l12 level1 lfo15;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span style='font-size:9.0pt;font-family:굴림;
mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:
굴림;color:black;mso-font-kerning:0pt'>회사의</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>사이트에</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>들어가</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>핵심</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>기술을</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>가져오자</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>!!&nbsp;&nbsp;</span><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_48" o:spid="_x0000_i1034"
 type="#_x0000_t75" style='width:451.5pt;height:231pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image028.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>주어진 링크인 <span lang=EN-US>sdhsroot.kro.kr/BlackOut/index.html</span>에
접속했다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_49" o:spid="_x0000_i1033"
 type="#_x0000_t75" style='width:451.5pt;height:223.5pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image029.png" o:title=""
  cropbottom="5626f"/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='margin-left:9.7pt;text-align:left;
text-indent:-9.7pt;mso-char-indent-count:-1.0;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>사이트 여기저기를 뒤져보다가 <span lang=EN-US>BLOG </span>메뉴의 <span
lang=EN-US>SINGLEPOST</span>에 가니 위와 같은 <span lang=EN-US>Article</span>이 나온다<span
lang=EN-US>.<o:p></o:p></span></span></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l9 level1 lfo16;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>http://sdhsroot.kro.kr/BlackOut/singlepost.html&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l9 level1 lfo16;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><b><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:#006699;mso-font-kerning:0pt'>&lt;h1&gt;</span></b><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>FLAG</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;/h1&gt;</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l9 level1 lfo16;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>3.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;div</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:red;mso-font-kerning:0pt'>class</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>=</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;article&quot;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&gt;</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l9 level1 lfo16;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>4.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;img</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:red;mso-font-kerning:0pt'>src</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>=</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;images/martianrover-journey.jpg&quot;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:red;mso-font-kerning:0pt'>alt</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>=</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;&quot;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&gt;</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l9 level1 lfo16;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>5.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;h1&gt;</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>MARTIAN&nbsp;ROVER&nbsp;JOURNEY</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;/h1&gt;</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l9 level1 lfo16;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>6.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;span&gt;</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>FEBRUARY&nbsp;6,&nbsp;2023</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;/span&gt;</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l9 level1 lfo16;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>7.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;p&gt;</span></b><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>지금은</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;2023</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>년</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>...&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>우리의</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>핵심기술을</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>잃어버렸다</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>.</span><b><span lang=EN-US style='font-size:
9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:
굴림;color:#006699;mso-font-kerning:0pt'>&lt;/p&gt;</span></b><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l9 level1 lfo16;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>8.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;p&gt;</span></b><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>아주아주</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>오래전</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>...&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>이</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>파일</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>안에는</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>우리의</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>핵심기술이</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>담겨있었습니다</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>.</span><b><span lang=EN-US style='font-size:
9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:
굴림;color:#006699;mso-font-kerning:0pt'>&lt;/p&gt;</span></b><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l9 level1 lfo16;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>9.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;p&gt;</span></b><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>하지만</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>페이지</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>디자인</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>작업중</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>정전이</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>나버렸고</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>,&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>이곳에</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>담겨있던</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>핵심기술은</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>날아가</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>버렸습니다</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>.</span><b><span lang=EN-US style='font-size:
9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:
굴림;color:#006699;mso-font-kerning:0pt'>&lt;/p&gt;</span></b><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l9 level1 lfo16;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>10.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;P&gt;</span></b><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>지금도</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>이</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>서버</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>어딘가에</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>핵심기술이</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>담겨있는</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>파일이</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>&nbsp;</span><span style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:
Consolas;mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>돌아다닐</span><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;</span><span style='font-size:9.0pt;
font-family:굴림;mso-ascii-font-family:Consolas;mso-hansi-font-family:Consolas;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>수</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>있습니다</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>.</span><b><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:
0pt'>&lt;/P&gt;</span></b><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;
mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span lang=EN-US style='font-size:
9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:
굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l9 level1 lfo16;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>11.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>&lt;/div&gt;</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='margin-left:9.7pt;text-align:left;
text-indent:-9.7pt;mso-char-indent-count:-1.0;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>‘</span><span style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>이 파일<span lang=EN-US>’</span>은 아마 <span
lang=EN-US>Article</span>에 있는 <span lang=EN-US>picture</span>나 <span
lang=EN-US>html file</span>을 의미하는 것이라고 생각하고 다운받아 살펴보고 <span lang=EN-US>hex code</span>도
확인하는 등 온갓 시도를 해보았고<span lang=EN-US>, </span>사이트에 있는 다른 파일들도 살펴보았다<span
lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='margin-left:9.7pt;text-align:left;
text-indent:-9.7pt;mso-char-indent-count:-1.0;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>그러다가 <span lang=EN-US>‘</span>정전<span lang=EN-US>(blackout)’</span>과
파일이 <span lang=EN-US>‘</span>날아갔다<span lang=EN-US>’, ‘</span>서버 어딘가에<span
lang=EN-US>’ </span>등으로 <span lang=EN-US>blackout </span>때문에 날아가버린<span
lang=EN-US> vi </span>에디터의 <span lang=EN-US>.swp </span>파일이 서버 어딘가에 남아있다는 것을 말해주려고
하는 것 같았다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='margin-left:9.7pt;text-align:left;
text-indent:-9.7pt;mso-char-indent-count:-1.0;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>그렇다면<span lang=EN-US> .swp </span>파일의 이름은 무엇일지 <span
lang=EN-US>guessing</span>해야 할 것이다<span lang=EN-US>. ‘.flag.txt.swp’ </span>등으로
<span lang=EN-US>Flag</span>와 관련하여 시도해보았지만 아니였다<span lang=EN-US>. <o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='margin-left:9.7pt;text-align:left;
text-indent:-9.7pt;mso-char-indent-count:-1.0;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>잠깐<span lang=EN-US>, ‘</span>이 파일<span lang=EN-US>’</span>이라고
했으므로 해당<span lang=EN-US> html file</span>과 관련되어 있지 않을까<span lang=EN-US>?<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='margin-left:9.7pt;text-align:left;
text-indent:-9.7pt;mso-char-indent-count:-1.0;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>sdhsroot.kro.kr/BlackOut/.singlepost.html.swp</span><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>에서 <span lang=EN-US>Flag</span>를 찾을 수 있었다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='margin-left:10.0pt;text-align:left;
text-indent:-10.0pt;mso-char-indent-count:-1.0;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_1" o:spid="_x0000_i1032"
 type="#_x0000_t75" style='width:450.75pt;height:361.5pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image030.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
background:lightgrey;mso-highlight:lightgrey;mso-no-proof:yes'>FLAG{FROM_2017_FLAG}</span><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'>WEBHACKING &#8211; </span></b><b
style='mso-bidi-font-weight:normal'><span style='font-size:14.0pt;font-family:
만화진흥원체;mso-no-proof:yes'>보물찾기<span lang=EN-US><o:p></o:p></span></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>이리저리 찾아보고 헤매다가 <span lang=EN-US>http://sdhsroot.kro.kr</span>의
구성요소를 모두 다운받아 하나의 폴더에 저장하고<span lang=EN-US>, </span>개발 중이였던 해킹 툴의 소스코드를 약간 수정하여
실행했더니<span lang=EN-US> Flag</span>가 나왔다<span lang=EN-US>. </span><s>뭐 이런</s> <span
lang=EN-US><o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_4" o:spid="_x0000_i1031"
 type="#_x0000_t75" style='width:368.25pt;height:64.5pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image031.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>다른 <span lang=EN-US>CTF</span>에서 파일의 <span lang=EN-US>hex
dump</span>에 <span lang=EN-US>Flag</span>를 숨겨놓는 간단한 문제들이 나오는 것을 여러 번 보았기 때문에 <span
lang=EN-US>Flag</span>값을 더 빨리 찾아낼 수 있도록 재미 삼아 만든 툴이다<span lang=EN-US>. </span>파일의
<span lang=EN-US>hex code</span>를 출력하고 <span lang=EN-US>Flag</span>에 자주 쓰이는 키워드<span
lang=EN-US>(Flag, FLAG, flag, ctf, CTF </span>등<span lang=EN-US>)</span>를 <span
lang=EN-US>hex code</span>에서 검색해 출력하는 기능까지 구현했는데<span lang=EN-US>, </span>파일명을 하나
입력받아 해당 파일명의 파일만 검색하는 것에서 같은 디렉토리 안의 파일 전체를 대상으로 검색하고 <span lang=EN-US>hex code
</span>출력 기능을 제거하여 사용했다<span lang=EN-US>. </span>보다시피 그냥 <span lang=EN-US>C</span>언어로
쉽게 프로그래밍이 가능한 툴이다<span lang=EN-US>. </span>코드는 생략<span lang=EN-US>(</span>잇힝<span
lang=EN-US>)<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_39" o:spid="_x0000_i1030"
 type="#_x0000_t75" style='width:451.5pt;height:140.25pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image032.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>저녀석에 따르면 </span><span lang=EN-US><a
href="http://sdhsroot.kro.kr/vendor/bootstrap/css/bootstrap.min.css"><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>http://sdhsroot.kro.kr/vendor/bootstrap/css/bootstrap.min.css</span></a></span><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>의 주석 부분에 있다는데<span lang=EN-US>, </span>상상도 못한 곳이다<span
lang=EN-US>. </span>깃허브 어쩌고길래 외부 모듈인 줄 알았는데<span lang=EN-US>. </span>문제 힌트에서 나는
모르는 무언가가 있었던 것일까<span lang=EN-US>.. </span>그냥 방심하지 말고 하나씩 차분하게 살펴보아야 하는 거구나<span
lang=EN-US>…<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><b
style='mso-bidi-font-weight:normal'><span lang=EN-US style='font-size:14.0pt;
font-family:만화진흥원체;mso-no-proof:yes'>WEBHACKING &#8211; Phishing<o:p></o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_6" o:spid="_x0000_i1029"
 type="#_x0000_t75" style='width:324.75pt;height:96.75pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image033.png" o:title=""/>
</v:shape></span><b style='mso-bidi-font-weight:normal'><span lang=EN-US
style='font-size:14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>주어진 링크를 클릭하면 부적절한 접근이라는 알림이 표시되면서 이전 페이지로 리디렉션된다<span
lang=EN-US>. <o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_7" o:spid="_x0000_i1028"
 type="#_x0000_t75" style='width:234pt;height:97.5pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image034.png" o:title=""/>
</v:shape></span><b style='mso-bidi-font-weight:normal'><span lang=EN-US
style='font-size:14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>크롬에서 페이지 주소의 앞부분에 <span lang=EN-US>‘view-source:’</span>를 붙이자
위와 같이 페이지 소스를 볼 수 있었고<span lang=EN-US>, </span>주석으로 <span lang=EN-US>asd.php</span>가
표시되어 있는 것 역시 확인이 가능했다<span lang=EN-US>.</span></span><span lang=EN-US
style='mso-no-proof:yes'><v:shape id="그림_x0020_9" o:spid="_x0000_i1027" type="#_x0000_t75"
 style='width:324pt;height:98.25pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="README.files/image035.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>sdhsroot.kro.kr/Phishing/asd.php</span><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>에 접속하자 위처럼<span lang=EN-US> FLAG{</span>코드속에<span lang=EN-US>…}</span>이라는<span
lang=EN-US> alart</span>가 나온다<span lang=EN-US>. </span>물론 해당 <span lang=EN-US>Flag</span>는
<span lang=EN-US>Fake</span>로<span lang=EN-US>, </span>인증이 되지 않는다<span
lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_8" o:spid="_x0000_i1026"
 type="#_x0000_t75" style='width:452.25pt;height:193.5pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image036.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>페이지 소스를 확인해 보니 난독화된 자바스크립트 코드가 있었다<span lang=EN-US>.<o:p></o:p></span></span></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><b><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:#006699;mso-font-kerning:0pt'>var</span></b><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;b&nbsp;=&nbsp;200;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><b><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:#006699;mso-font-kerning:0pt'>for</span></b><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;=&nbsp;0;&nbsp;a&nbsp;&lt;=&nbsp;20;&nbsp;a++)&nbsp;{&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>3.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;b&nbsp;=&nbsp;b&nbsp;+&nbsp;((a&nbsp;*&nbsp;b)&nbsp;-&nbsp;(a&nbsp;/&nbsp;b));&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>4.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;0)&nbsp;b&nbsp;=&nbsp;70;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>5.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;1)&nbsp;b&nbsp;=&nbsp;76;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>6.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;3)&nbsp;b&nbsp;=&nbsp;71;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>7.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;2)&nbsp;b&nbsp;=&nbsp;65;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>8.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;4)&nbsp;b&nbsp;=&nbsp;123;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>9.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;20)&nbsp;b&nbsp;=&nbsp;125;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>10.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;5)&nbsp;{&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>11.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>continue</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>12.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;6)&nbsp;{&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>13.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alert(</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:
0pt'>코</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:
0pt'>&quot;</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>);&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#5C5C5C;
mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>14.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>continue</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>15.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;7)&nbsp;{&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>16.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alert(</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:
0pt'>드</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:
0pt'>&quot;</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>);&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#5C5C5C;
mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>17.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>continue</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>18.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;8)&nbsp;{&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>19.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alert(</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:
0pt'>속</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:
0pt'>&quot;</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>);&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#5C5C5C;
mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>20.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>continue</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>21.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;9)&nbsp;{&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>22.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alert(</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;</span><span
style='font-size:9.0pt;font-family:굴림;mso-ascii-font-family:Consolas;
mso-hansi-font-family:Consolas;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:
0pt'>에</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:
0pt'>&quot;</span><span lang=EN-US style='font-size:9.0pt;font-family:Consolas;
mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:
0pt'>);&nbsp;&nbsp;</span><span lang=EN-US style='font-size:9.0pt;font-family:
Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;color:#5C5C5C;
mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>23.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>continue</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>24.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;10)&nbsp;{&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>25.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alert(</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;.&quot;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>);&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>26.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>continue</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>27.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;11)&nbsp;{&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>28.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alert(</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;.&quot;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>);&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>29.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>continue</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>30.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;12)&nbsp;{&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>31.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alert(</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:blue;mso-font-kerning:0pt'>&quot;.&quot;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>);&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>32.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>continue</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>33.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;&gt;=&nbsp;4&nbsp;&amp;&amp;&nbsp;a&nbsp;&lt;=&nbsp;20)&nbsp;{&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>34.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>continue</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>35.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>36.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;alert(String.fromCharCode(b))&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l10 level1 lfo17;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>37.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>}&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>jsbeautifier.org</span><span style='font-size:11.0pt;
mso-bidi-font-size:14.0pt;font-family:만화진흥원체;mso-no-proof:yes'>에서 난독화를 해제하자 위와 같은
코드가 나타났다<span lang=EN-US>.<o:p></o:p></span></span></p>

<div style='mso-element:para-border-div;border:none;border-left:solid #6CE26C 2.25pt;
padding:0cm 0cm 0cm 0cm;background:white;margin-left:18.0pt;margin-right:0cm'>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>1.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&lt;script&gt;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>2.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><b><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:#006699;mso-font-kerning:0pt'>var</span></b><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;b&nbsp;=&nbsp;200;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>3.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><b><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:#006699;mso-font-kerning:0pt'>for</span></b><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:굴림;
mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;=&nbsp;0;&nbsp;a&nbsp;&lt;=&nbsp;20;&nbsp;a++)&nbsp;{&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>4.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;b&nbsp;=&nbsp;b&nbsp;+&nbsp;((a&nbsp;*&nbsp;b)&nbsp;-&nbsp;(a&nbsp;/&nbsp;b));&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>5.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;0)&nbsp;b&nbsp;=&nbsp;70;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>6.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;1)&nbsp;b&nbsp;=&nbsp;76;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>7.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;3)&nbsp;b&nbsp;=&nbsp;71;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>8.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;2)&nbsp;b&nbsp;=&nbsp;65;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>9.<span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;
</span></span></span><![endif]><span lang=EN-US style='font-size:9.0pt;
font-family:Consolas;mso-fareast-font-family:굴림;mso-bidi-font-family:굴림;
color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;4)&nbsp;b&nbsp;=&nbsp;123;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>10.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>else</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;</span><b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#006699;mso-font-kerning:0pt'>if</span></b><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;(a&nbsp;==&nbsp;20)&nbsp;b&nbsp;=&nbsp;125;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>11.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&nbsp;&nbsp;&nbsp;&nbsp;document.write(String.fromCharCode(b))&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:#F8F8F8;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>12.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>}&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='mso-margin-top-alt:auto;mso-margin-bottom-alt:
auto;margin-left:18.0pt;text-align:left;text-indent:-18.0pt;line-height:10.5pt;
mso-pagination:widow-orphan;mso-list:l15 level1 lfo18;tab-stops:list 36.0pt;
background:white;text-autospace:ideograph-numeric ideograph-other;word-break:
keep-all;border:none;mso-border-left-alt:solid #6CE26C 2.25pt;padding:0cm;
mso-padding-alt:0cm 0cm 0cm 0cm'><![if !supportLists]><span lang=EN-US
style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:Consolas;
mso-bidi-font-family:Consolas;color:#5C5C5C;mso-font-kerning:0pt'><span
style='mso-list:Ignore'>13.<span style='font:7.0pt "Times New Roman"'> </span></span></span><![endif]><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:black;mso-font-kerning:0pt'>&lt;/script&gt;&nbsp;&nbsp;</span><span
lang=EN-US style='font-size:9.0pt;font-family:Consolas;mso-fareast-font-family:
굴림;mso-bidi-font-family:굴림;color:#5C5C5C;mso-font-kerning:0pt'><o:p></o:p></span></p>

</div>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
style='font-size:11.0pt;mso-bidi-font-size:14.0pt;font-family:만화진흥원체;
mso-no-proof:yes'>위와 같이 코드를 수정한 뒤 <span lang=EN-US>js.do</span>에서 실행하자 문제의 힌트에서처럼
깨진 문자열로 이루어진 <span lang=EN-US>Flag</span>가 나왔다<span lang=EN-US>.<o:p></o:p></span></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='mso-no-proof:yes'><v:shape id="그림_x0020_50" o:spid="_x0000_i1025"
 type="#_x0000_t75" style='width:180.75pt;height:21pt;visibility:visible;
 mso-wrap-style:square'>
 <v:imagedata src="README.files/image037.png" o:title=""/>
</v:shape></span><span lang=EN-US style='font-size:11.0pt;mso-bidi-font-size:
14.0pt;font-family:만화진흥원체;mso-no-proof:yes'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;line-height:normal'><span
lang=EN-US style='font-size:11.0pt;font-family:만화진흥원체;color:black;background:
lightgrey;mso-highlight:lightgrey'>FLAG{</span><span lang=EN-US
style='font-size:11.0pt;font-family:"Calibri",sans-serif;mso-fareast-font-family:
만화진흥원체;color:black;background:lightgrey;mso-highlight:lightgrey'>&#737;</span><span
lang=EN-US style='font-size:11.0pt;font-family:"Gadugi",sans-serif;mso-fareast-font-family:
만화진흥원체;mso-bidi-font-family:Gadugi;color:black;background:lightgrey;mso-highlight:
lightgrey'>&#5165;</span><span style='font-size:11.0pt;font-family:"Microsoft Yi Baiti";
mso-bidi-font-family:"Microsoft Yi Baiti";color:black;background:lightgrey;
mso-highlight:lightgrey'>&#41325;</span><span style='font-size:11.0pt;font-family:
만화진흥원체;mso-bidi-font-family:"맑은 고딕";color:black;background:lightgrey;
mso-highlight:lightgrey'>곚삍</span><span style='font-size:11.0pt;mso-ascii-font-family:
"맑은 고딕";mso-fareast-font-family:"맑은 고딕";mso-hansi-font-family:"맑은 고딕";
mso-bidi-font-family:"맑은 고딕";color:black;background:lightgrey;mso-highlight:
lightgrey'>&#17936;&#18631;</span><span style='font-size:11.0pt;font-family:만화진흥원체;
mso-bidi-font-family:만화진흥원체;color:black;background:lightgrey;mso-highlight:
lightgrey'>눛뵼<span lang=EN-US>&#6734;</span></span><span lang=EN-US style='font-size:
11.0pt;font-family:"Segoe UI",sans-serif;mso-fareast-font-family:만화진흥원체;
color:black;background:lightgrey;mso-highlight:lightgrey'>&#42216;</span><span
style='font-size:11.0pt;font-family:만화진흥원체;color:black;background:lightgrey;
mso-highlight:lightgrey'>&#62315;</span><span lang=EN-US style='font-size:11.0pt;
font-family:"Calibri",sans-serif;mso-fareast-font-family:만화진흥원체;color:black;
background:lightgrey;mso-highlight:lightgrey'>&#7568;</span><span lang=EN-US
style='font-size:11.0pt;font-family:"Microsoft JhengHei",sans-serif;mso-bidi-font-family:
"Microsoft JhengHei";color:black;background:lightgrey;mso-highlight:lightgrey'>&#12720;</span><span
style='font-size:11.0pt;font-family:만화진흥원체;color:black;background:lightgrey;
mso-highlight:lightgrey'>&#57856;<span lang=EN-US>}<o:p></o:p></span></span></p>

</div>

</body>

</html>
