#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import defaultdict
import urllib , requests , re , os , json , uuid , base64 , cfscrape , kodi4vn , io
import concurrent . futures
from kodiswift import Plugin
from kodi_six import xbmc
from operator import itemgetter
from cookielib import LWPCookieJar
requests . packages . urllib3 . disable_warnings ( )
if 64 - 64: i11iIiiIii
OO0o = Plugin ( )
Oo0Ooo = cfscrape . create_scraper ( )
Oo0Ooo . cookies = LWPCookieJar ( )
if 85 - 85: OOO0O0O0ooooo % IIii1I . II1 - O00ooooo00
I1IiiI = 30
IIi1IiiiI1Ii = "plugin://plugin.video.hpo1988.fcine"
I11i11Ii = IIi1IiiiI1Ii . split ( "/" ) [ - 1 ]
oO00oOo = "https://docs.google.com/drawings/d/12OjbFr3Z5TCi1WREwTWECxNNwx0Kx-FTrCLOigrpqG4/pub?w=256&h=256"
OOOo0 = "https://docs.google.com/drawings/d/1rniOY_omlvmXtpuHFoMuCS3upWOu04DD0KWRyLV4szs/pub?w=1920&h=1080"
Oooo000o = '<div class="esnList_item">.+?<a href="(.+?)"[^>]*><img[^>]*src="(.+?)"></a>.+?<a[^>]*title="(.+?)">'
IiIi11iIIi1Ii = '<div class="esnList_item">.+?<a href="(.+?)"[^>]*><img[^>]*src="(.+?)"></a>.+?<a[^>]*title="(.+?)">'
if 54 - 54: IIIiiIIii / o0oo0oo0OO00 . iI111iI / oOOo + I1Ii111
if 93 - 93: iiI1i1 . II1ii1II1iII1 + oO0o . oOOOO0o0o . o0oO0 + oo00
o00 = {
 'Cookie' : ''
 }
if 62 - 62: II1ii - o0oOoO00o . iIi1IIii11I + oo0 * o0oOoO00o % o0oOoO00o
if 22 - 22: oo00 . o0oOoO00o
@ OO0o . route ( '/' )
def I11 ( ) : pass
if 98 - 98: i11iIiiIii * o0oo0oo0OO00 % II1ii * II1ii * IIIiiIIii
if 79 - 79: o0oOoO00o
if 86 - 86: I1Ii111 % o0oo0oo0OO00
@ OO0o . route ( '/search' )
def oo ( ) :
 IiII1I1i1i1ii = OO0o . keyboard ( heading = 'Tìm kiếm' )
 if IiII1I1i1i1ii :
  IiII1I1i1i1ii = IiII1I1i1i1ii . decode ( "utf8" , "ignore" )
  IIIII = 'https://fcine.net/findContent/?videobox=&term={0}&page=%s' . format ( IiII1I1i1i1ii . replace ( " " , "+" ) ) . encode ( "utf8" , "ignore" )
  with io . open ( kodi4vn . SEARCH_HISTORY_PATH , "a" , encoding = "utf-8" ) as I1 :
   I1 . write ( IiII1I1i1i1ii + "\n" )
  O0OoOoo00o = {
 "title" : "Search: {0}" . format ( IiII1I1i1i1ii ) . encode ( "utf8" , "ignore" ) ,
 "url" : IIIII ,
 "page" : 1
 }
  iiiI11 = '{0}/list_media/{1}' . format (
 IIi1IiiiI1Ii ,
 urllib . quote_plus ( json . dumps ( O0OoOoo00o ) )
 )
  OO0o . redirect ( iiiI11 )
  if 91 - 91: iiI1i1 / IIIiiIIii . II1ii1II1iII1 + oOOOO0o0o
@ OO0o . route ( '/searchlist' )
def iI11 ( ) :
 iII111ii = [ ]
 i1iIIi1 = [ {
 "label" : "[B]Search[/B]" ,
 "path" : "{0}/search" . format ( IIi1IiiiI1Ii ) ,
 "thumbnail" : "https://docs.google.com/drawings/d/1uP5xm3I5KRZsnoliqJDkYJXYz1MznecVqWg3e-Gue48/pub?w=256&h=256"
 } ]
 ii11iIi1I = [ ]
 if os . path . exists ( kodi4vn . SEARCH_HISTORY_PATH ) :
  with io . open ( kodi4vn . SEARCH_HISTORY_PATH , "r" , encoding = "utf-8" ) as I1 :
   ii11iIi1I = I1 . read ( ) . strip ( ) . split ( "\n" )
  for iI111I11I1I1 in reversed ( ii11iIi1I ) :
   IIIII = 'https://fcine.net/findContent/?videobox=&term=' + iI111I11I1I1 . replace ( " " , "+" ) + '&page=%s'
   O0OoOoo00o = {
 "title" : "Search: {0}" . format ( iI111I11I1I1 ) ,
 "url" : IIIII ,
 "page" : 1
 }
   OOooO0OOoo = { }
   OOooO0OOoo [ "label" ] = iI111I11I1I1
   OOooO0OOoo [ "path" ] = "{0}/list_media/{1}" . format (
 IIi1IiiiI1Ii ,
 urllib . quote_plus ( json . dumps ( O0OoOoo00o ) )
 )
   OOooO0OOoo [ "thumbnail" ] = "https://docs.google.com/drawings/d/1uP5xm3I5KRZsnoliqJDkYJXYz1MznecVqWg3e-Gue48/pub?w=256&h=256"
   iII111ii . append ( OOooO0OOoo )
 iII111ii = i1iIIi1 + iII111ii
 OO0o . set_content ( "files" )
 return OO0o . finish ( iII111ii )
 if 29 - 29: iiI1i1 / IIii1I
@ OO0o . route ( '/list_media/<args_json>' )
def IiIIIiI1I1 ( args_json = { } ) :
 iII111ii = [ ]
 OoO000 = json . loads ( args_json )
 kodi4vn . GA ( I11i11Ii , kodi4vn . GA_MEDIA , OoO000 )
 IIiiIiI1 = kodi4vn . Request ( OoO000 [ "url" ] % OoO000 [ "page" ] , session = Oo0Ooo , mobile = True )
 iiIiIIi = kodi4vn . cleanHTML ( IIiiIiI1 . text )
 ooOoo0O = re . compile ( Oooo000o ) . findall ( iiIiIIi )
 for IIIII , OooO0 , II11iiii1Ii in ooOoo0O :
  O0OoOoo00o = {
 "title" : II11iiii1Ii ,
 "quality_label" : "" ,
 "url" : IIIII
 }
  OOooO0OOoo = { }
  OOooO0OOoo [ "label" ] = II11iiii1Ii
  OOooO0OOoo [ "path" ] = "{0}/list_mirrors/{1}" . format (
 IIi1IiiiI1Ii ,
 urllib . quote_plus ( json . dumps ( O0OoOoo00o ) )
 )
  OOooO0OOoo [ "thumbnail" ] = OooO0
  iII111ii . append ( OOooO0OOoo )
 if len ( iII111ii ) == I1IiiI :
  OO0oOoo = int ( OoO000 [ "page" ] ) + 1
  OoO000 [ "page" ] = OO0oOoo
  iII111ii . append ( {
 'label' : 'Next >>' ,
 'path' : '{0}/list_media/{1}' . format (
 IIi1IiiiI1Ii ,
 urllib . quote_plus ( json . dumps ( OoO000 ) )
 ) ,
 'thumbnail' : oO00oOo
 } )
 OO0o . set_content ( "movies" )
 return OO0o . finish ( iII111ii )
 if 68 - 68: o0oO0 + oOOOO0o0o . IIii1I - o0oOoO00o % IIii1I - oo0
 if 79 - 79: iI111iI + o0oo0oo0OO00 - II1ii
@ OO0o . route ( '/list_mirrors/<args_json>' )
def oO00O00o0OOO0 ( args_json = { } ) :
 iII111ii = [ ]
 OoO000 = json . loads ( args_json )
 kodi4vn . GA ( I11i11Ii , kodi4vn . GA_MIRROR , OoO000 )
 O0OoOoo00o = {
 "title" : OoO000 [ "title" ] ,
 "quality_label" : OoO000 [ "quality_label" ] ,
 "mirror" : "Default server" ,
 "url" : OoO000 [ "url" ]
 }
 Ii1iIIIi1ii = '{0}/list_eps/{1}' . format (
 IIi1IiiiI1Ii ,
 urllib . quote_plus ( json . dumps ( O0OoOoo00o ) )
 )
 OO0o . set_content ( "files" )
 OO0o . redirect ( Ii1iIIIi1ii )
 if 80 - 80: o0oO0 * i11iIiiIii / iIi1IIii11I
 if 9 - 9: oo00 + oO0o % oo00 + O00ooooo00 . oOOOO0o0o
@ OO0o . route ( '/list_eps/<args_json>' )
def III1i1i ( args_json = { } ) :
 iII111ii = [ ]
 OoO000 = json . loads ( args_json )
 kodi4vn . GA ( I11i11Ii , kodi4vn . GA_EPS , OoO000 )
 IIiiIiI1 = kodi4vn . Request ( "https://docs.google.com/spreadsheets/u/7/d/13VzQebjGYac5hxe1I-z1pIvMiNB0gSG7oWJlFHWnqsA/export?format=tsv&gid=2064177887" )
 o00 [ "Cookie" ] = IIiiIiI1 . text . decode ( 'base64' )
 IIiiIiI1 = kodi4vn . Request ( OoO000 [ "url" ] , additional_headers = o00 , session = Oo0Ooo )
 iiIiIIi = kodi4vn . cleanHTML ( IIiiIiI1 . text ) . encode ( "utf8" )
 iiI1 = ""
 try :
  iiI1 = re . search ( 'href="(https\://fcine.net/\?app=videobox.+?)"' , iiIiIIi ) . group ( 1 )
 except : pass
 i11Iiii = re . compile ( r'<a href="(https\://www.fshare.vn/file/.+?)"[^>]*>(.+?)</p>' ) . findall ( iiIiIIi )
 if 23 - 23: iiI1i1 . IIIiiIIii
 for Oo0O0OOOoo , oOoOooOo0o0 in i11Iiii :
  oOoOooOo0o0 = re . sub ( '<[^>]*>' , '' , oOoOooOo0o0 . decode ( "utf8" ) ) . strip ( ) . replace ( "</a>" , "" )
  O0OoOoo00o = {
 "title" : OoO000 [ "title" ] ,
 "quality_label" : OoO000 [ "quality_label" ] ,
 "mirror" : OoO000 [ "mirror" ] ,
 "url" : Oo0O0OOOoo ,
 "sub" : iiI1 ,
 "eps" : oOoOooOo0o0
 }
  OOooO0OOoo = { }
  OOooO0OOoo [ "label" ] = u"{0} - {1} ({2}) [{3}]" . format (
 oOoOooOo0o0 ,
 OoO000 [ "title" ] ,
 OoO000 [ "quality_label" ] ,
 OoO000 [ "mirror" ]
 )
  OOooO0OOoo [ "path" ] = '{0}/play/{1}/{2}' . format (
 IIi1IiiiI1Ii ,
 urllib . quote_plus ( json . dumps ( O0OoOoo00o ) ) ,
 OoO000 [ "title" ]
 )
  OOooO0OOoo [ "is_playable" ] = True
  try :
   OOooO0OOoo [ "info" ] = {
 "title" : re . search ( r'^(.+?) \(\d+\)' , OoO000 [ "title" ] ) . group ( 1 ) . split ( " - " ) [ 0 ] ,
 "year" : re . search ( r'^.+? \((\d+)\)' , OoO000 [ "title" ] ) . group ( 1 ) ,
 "type" : "video"
 }
  except :
   OOooO0OOoo [ "info" ] = { "type" : "video" }
  iII111ii . append ( OOooO0OOoo )
 OO0o . set_content ( "episodes" )
 return OO0o . finish ( iII111ii )
 if 61 - 61: iiI1i1 / oOOo + oo0 * oO0o / oO0o
@ OO0o . route ( '/play/<args_json>/<title>' )
def OoOo ( args_json = { } , title = "" ) :
 OoO000 = json . loads ( args_json )
 kodi4vn . GA ( I11i11Ii , kodi4vn . GA_PLAY , OoO000 )
 OO0o . set_resolved_url ( iI ( OoO000 [ "url" ] ) , subtitles = OoO000 [ "sub" ] )
 if 60 - 60: o0oO0 / o0oO0
 if 46 - 46: oo00 * oOOOO0o0o - oOOo * oO0o - iIi1IIii11I
def iI ( url ) :
 iiiI11 = "plugin://plugin.video.hpo1988.playlist/play/{}/{}" . format (
 urllib . quote_plus ( re . sub ( '\?token=.+?$' , '' , url ) ) ,
 urllib . quote_plus ( "Unknown" )
 )
 xbmc . log ( url , 7 )
 return iiiI11
 if 83 - 83: II1
 if 31 - 31: IIIiiIIii - oOOOO0o0o . iIi1IIii11I % I1Ii111 - OOO0O0O0ooooo
if __name__ == '__main__' :
 OO0o . run ( ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
