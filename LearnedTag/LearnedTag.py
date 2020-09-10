# -*- coding: utf-8 -*-
# Copyright: Luminous Spice <luminous.spice@gmail.com>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/copyleft/agpl.html
#
# This simple Add-on automatically adds a tag on your mature notes after the review.
# GitHub: https://github.com/luminousspice/anki-addons/

#This is a simple modification of the above add-on to tag a card and fill a field (if you have such a field), which represents knowing a card well enough to switch templates, reverse it, study the content elsewhere, etc. 
#By default the setting is 7 but I think anywhere under two weeks should work well. You can use 'selective card generation' (see Anki manual) to automatically create new cards of a certain template style when the field is filled.

from anki.hooks import wrap
from anki.sched import Scheduler
from aqt import mw

# Threshold learned interval
threshold = 10 # days

# Tag string for learned note
LearnedTag = u"Learned"
def learnedCheck(self, card, ease):
    f = card.note()
    if (card.ivl >= threshold):
        f.addTag(LearnedTag)
        if 'Learned' in mw.col.models.fieldNames(f.model()): # if field exists
            if not f[ 'Learned' ]: # if field is empty
                f[ 'Learned' ] = 'Yes'
    f.flush()
    return True

Scheduler.answerCard = wrap(Scheduler.answerCard, learnedCheck)
from anki.schedv2 import Scheduler as SchedulerV2
SchedulerV2.answerCard = wrap(SchedulerV2.answerCard, learnedCheck)