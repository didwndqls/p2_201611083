﻿speechA=["AT this second appearing to take the oath of the Presidential office there is less occasion for an extended address than there was at the first",
       "Then a statement somewhat in detail of a course to be pursued seemed fitting and proper",
       "Now at the expiration of four years during which public declarations have been constantly called forth on every point and phase of the great contest which still absorbs the attention and engrosses the energies of the nation little that is new could be presented",
       "The progress of our arms upon which all else chiefly depends is as well known to the public as to myself and it is I trust reasonably satisfactory and encouraging to all",
       "With high hope for the future no prediction in regard to it is ventured",
       "On the occasion corresponding to this four years ago all thoughts were anxiously directed to an impending civil war",
       "All dreaded it all sought to avert it",
       "While the inaugural address was being delivered from this place devoted altogether to saving the Union without war urgent agents were in the city seeking to destroy it without war  seeking to dissolve the Union and divide effects by negotiation",
       "Both parties deprecated war but one of them would make war rather than let the nation survive and the other would accept war rather than let it perish, and the war came",
       "One eighth of the whole population were colored slaves not distributed generally over the Union but localized in the southern part of it", 
       "These slaves constituted a peculiar and powerful interest",
       "All knew that this interest was somehow the cause of the war",
       "To strengthen perpetuate and extend this interest was the object for which the insurgents would rend the Union even by war while the Government claimed no right to do more than to restrict the territorial enlargement of it",
       "Neither party expected for the war the magnitude or the duration which it has already attained",
       "Neither anticipated that the cause of the conflict might cease with or even before the conflict itself should cease",
       "Each looked for an easier triumph and a result less fundamental and astounding",
       "Both read the same Bible and pray to the same God and each invokes His aid against the other",
       "It may seem strange that any men should dare to ask a just God's assistance in wringing their bread from the sweat of other men's faces but let us judge not that we be not judged",
       "The prayers of both could not be answered That of neither has been answered fully",
       "The Almighty has His own purposes",
       "Woe unto the world because of offenses for it must needs be that offenses come but woe to that man by whom the offense cometh",
       "If we shall suppose that American slavery is one of those offenses which in the providence of God, must needs come but which having continued through His appointed time He now wills to remove and that He gives to both North and South this terrible war as the woe due to those by whom the offense came shall we discern therein any departure from those divine attributes which the believers in a living God always ascribe to Him",
       "Fondly do we hope fervently do we pray that this mighty scourge of war may speedily pass away",
       "Yet if God wills that it continue until all the wealth piled by the bondsman's two hundred and fifty years of unrequited toil shall be sunk, and until every drop of blood drawn with the lash shall be paid by another drawn with the sword as was said three thousand years ago so still it must be said the judgments of the Lord are true and righteous altogether",
       "With malice toward none with charity for all with firmness in the right as God gives us to see the right let us strive on to finish the work we are in to bind up the nation's wounds to care for him who shall have borne the battle and for his widow and his orphan to do all which may achieve and cherish a just and lasting peace among ourselves and with all nations"]

def countWords():
    d = {}
    for line in speechA:
        words=line.split()
        for word in words:
            if word in d:
                d[word]+=1
            else:
                d[word]=1
    return d
def FrequentWords(c,d):
    wdA=list()
    for i in d:
        if d[i]>c:
            wdA.append(i)
    return wdA
word=countWords()
Frewords=FrequentWords(8,word)
print "Licoln speech Frequent words:", Frewords

speechB= ['Vice President Cheney Mr Chief Justice President Carter President Bush President Clinton reverend clergy distinguished guests fellow citizens',
        'On this day prescribed by law and marked by ceremony we celebrate the durable wisdom of our Constitution and recall the deep commitments that unite our country',
        'I am grateful for the honor of this hour mindful of the consequential times in which we live and determined to fulfill the oath that I have sworn and you have witnessed ',
        'At this second gathering our duties are defined not by the words I use but by the history we have seen together',
        'For a half century America defended our own freedom by standing watch on distant borders',
        'After the shipwreck of communism came years of relative quiet years of repose years of sabbatical ?and then there came a day of fire',
        'We have seen our vulnerability ?and we have seen its deepest source' ,
        'For as long as whole regions of the world simmer in resentment and tyranny ?prone to ideologies that feed hatred and excuse murder ? violence will gather and multiply in destructive power and cross the most defended borders and raise a mortal threat',
        'There is only one force of history that can break the reign of hatred and resentment and expose the pretensions of tyrants and reward the hopes of the decent and tolerant and that is the force of human freedom ',
        'We are led by events and common sense to one conclusion:' ,
        'The survival of liberty in our land increasingly depends on the success of liberty in other lands',
        'The best hope for peace in our world is the expansion of freedom in all the world',
        "America's vital interests and our deepest beliefs are now one",
        'From the day of our Founding we have proclaimed that every man and woman on this earth has rights and dignity and matchless value because they bear the image of the Maker of Heaven and earth',
        "Across the generations we have proclaimed the imperative of self-government because no one is fit to be a master and no one deserves to be a slave Advancing these ideals is the mission that created our Nation",
        "It is the honorable achievement of our fathers",
        "Now it is the urgent requirement of our nation's security and the calling of our time",
        'So it is the policy of the United States to seek and support the growth of democratic movements and institutions in every nation and culture with the ultimate goal of ending tyranny in our world',
        'This is not primarily the task of arms though we will defend ourselves and our friends by force of arms when necessary',
        'Freedom by its nature must be chosen and defended by citizens and sustained by the rule of law and the protection of minorities',
        'And when the soul of a nation finally speaks the institutions that arise may reflect customs and traditions very different from our own',
        'America will not impose our own style of government on the unwilling',
        'Our goal instead is to help others find their own voice attain their own freedom and make their own way ',
        "The great objective of ending tyranny is the concentrated work of generations" ,
        "The difficulty of the task is no excuse for avoiding it" "America's influence is not unlimited but fortunately for the oppressed America's influence is considerable and we will use it confidently in freedom's cause",
        "My most solemn duty is to protect this nation and its people against further attacks and emerging threats" ,
        "Some have unwisely chosen to test America's resolve and have found it firm ",
        'We will persistently clarify the choice before every ruler and every nation: The moral choice between oppression which is always wrong and freedom which is eternally right' 
        "America will not pretend that jailed dissidents prefer their chains or that women welcome humiliation and servitude or that any human being aspires to live at the mercy of bullies ",
        "We will encourage reform in other governments by making clear that success in our relations will require the decent treatment of their own people",
        " America's belief in human dignity will guide our policies yet rights must be more than the grudging concessions of dictators; they are secured by free dissent and the participation of the governed",
        'In the long run there is no justice without freedom and there can be no human rights without human liberty',
        'Some I know have questioned the global appeal of liberty ?though this time in history four decades defined by the swiftest advance of freedom ever seen is an odd time for doubt',
        "Americans of all people should never be surprised by the power of our ideals",
        "Eventually the call of freedom comes to every mind and every soul We do not accept the existence of permanent tyranny because we do not accept the possibility of permanent slavery Liberty will come to those who love it",
        'Today America speaks anew to the peoples of the world:',
        'All who live in tyranny and hopelessness can know: the United States will not ignore your oppression or excuse your oppressors' ,
        'When you stand for your liberty we will stand with you ',
        'Democratic reformers facing repression prison or exile can know: America sees you for who you are: the future leaders of your free country ',
        'The rulers of outlaw regimes can know that we still believe as Abraham Lincoln did:',
        "Those who deny freedom to others deserve it not for themselves; and under the rule of a just God cannot long retain it" ,
        'The leaders of governments with long habits of control need to know: To serve your people you must learn to trust them',
        'Start on this journey of progress and justice and America will walk at your side ',
        "And all the allies of the United States can know: we honor your friendship we rely on your counsel and we depend on your help",
        "Division among free nations is a primary goal of freedom's enemies",
        "The concerted effort of free nations to promote democracy is a prelude to our enemies' defeat",
        'Today I also speak anew to my fellow citizens: ',
        'From all of you I have asked patience in the hard task of securing America which you have granted in good measure',
        'Our country has accepted obligations that are difficult to fulfill and would be dishonorable to abandon',
        'Yet because we have acted in the great liberating tradition of this nation tens of millions have achieved their freedom',
        'And as hope kindles hope millions more will find it' ,
        'By our efforts we have lit a fire as well ?a fire in the minds of men',
        'It warms those who feel its power it burns those who fight its progress and one day this untamed fire of freedom will reach the darkest corners of our world ',
        'A few Americans have accepted the hardest duties in this cause ?in the quiet work of intelligence and diplomacy  the idealistic work of helping raise up free governments  the dangerous and necessary work of fighting our enemies',
        'Some have shown their devotion to our country in deaths that honored their whole lives ?and we will always honor their names and their sacrifice ',
        'All Americans have witnessed this idealism and some for the first time' ,
        'I ask our youngest citizens to believe the evidence of your eyes',
        'You have seen duty and allegiance in the determined faces of our soldiers',
        'You have seen that life is fragile and evil is real and courage triumphs',
        'Make the choice to serve in a cause larger than your wants larger than yourself ?and in your days you will add not just to the wealth of our country but to its character ',
        'America has need of idealism and courage because we have essential work at home ?the unfinished work of American freedom',
        'In a world moving toward liberty we are determined to show the meaning and promise of liberty ',
        "In America's ideal of freedom citizens find the dignity and security of economic independence instead of laboring on the edge of subsistence",
        "This is the broader definition of liberty that motivated the Homestead Act the Social Security Act and the GI Bill of Rights",
        ' And now we will extend this vision by reforming great institutions to serve the needs of our time',
        'To give every American a stake in the promise and future of our country we will bring the highest standards to our schools and build an ownership society',
        'We will widen the ownership of homes and businesses retirement savings and health insurance ?preparing our people for the challenges of life in free society',
        ' By making every citizen an agent of his or her own destiny we will give our fellow Americans greater freedom from want and fear and make our society more prosperous and just and equal',
        "In America's ideal of freedom the public interest depends on private character ?on integrity and tolerance toward others and the rule of conscience in our own lives",
        'Self-government relies in the end on the governing of the self',
        ' That edifice of character is built in families supported by communities with standards and sustained in our national life by the truths of Sinai the Sermon on the Mount the words of the Koran and the varied faiths of our people',
        "Americans move forward in every generation by reaffirming all that is good and true that came before ?ideals of justice and conduct that are the same yesterday today and forever ",
        "In America's ideal of freedom the exercise of rights is ennobled by service and mercy and a heart for the weak",
        'Liberty for all does not mean independence from one another',
        ' Our nation relies on men and women who look after a neighbor and surround the lost with love',
        ' Americans at our best value the life we see in one another and must always remember that even the unwanted have worth',
        "And our country must abandon all the habits of racism because we cannot carry the message of freedom and the baggage of bigotry at the same time ",
        'From the perspective of a single day including this day of dedication the issues and questions before our country are many',
        'From the viewpoint of centuries the questions that come to us are narrowed and few Did our generation advance the cause of freedom?',
        'And did our character bring credit to that cause? ',
        'These questions that judge us also unite us because Americans of every party and background Americans by choice and by birth are bound to one another in the cause of freedom',
        'We have known divisions which must be healed to move forward in great purposes ?and I will strive in good faith to heal them',
        ' Yet those divisions do not define America',
        'We felt the unity and fellowship of our nation when freedom came under attack and our response came like a single hand over a single heart',
        ' And we can feel that same unity and pride whenever America acts for good and the victims of disaster are given hope and the unjust encounter justice and the captives are set free ',
        'We go forward with complete confidence in the eventual triumph of freedom',
        'Not because history runs on the wheels of inevitability; it is human choices that move events',
        'Not because we consider ourselves a chosen nation; God moves and chooses as He wills' ,
        'We have confidence because freedom is the permanent hope of mankind the hunger in dark places the longing of the soul',
        'When our Founders declared a new order of the ages; when soldiers died in wave upon wave for a union based on liberty; when citizens marched in peaceful outrage under the banner "Freedom Now" ?they were acting on an ancient hope that is meant to be fulfilled',
        'History has an ebb and flow of justice but history also has a visible direction set by liberty and the Author of Liberty ',
        'When the Declaration of Independence was first read in public and the Liberty Bell was sounded in celebration a witness said "It rang as if it meant something" In our time it means something still', 
        'America in this young century proclaims liberty throughout all the world and to all the inhabitants thereof Renewed in our strength ? tested but not weary ? we are ready for the greatest achievements in the history of freedom ',
        'May God bless you and may He watch over the United States of America ']

def CWords():
    d = {}
    for line in speechB:
        words=line.split()
        for word in words:
            if word in d:
                d[word]+=1
            else:
                d[word]=1
    return d
def FWords(b,d):
    words=list()
    for c in d:
        if d[c]>b:
            words.append(c)
    return words
wordK=CWords()
Rword=FWords(23,wordK)
print "Bush Speech Frequent words:", Rword
input()
