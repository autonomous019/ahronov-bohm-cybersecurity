# ahronov-bohm-cybersecurity

<b>Synopsis:</b>

This project is aimed at Blue Team cybersecurity regarding the noosphere, the mind, or nouscurity, it can be applied to hardware such as embeded medical devices and wetware, such as the brain itself. It is based on the scientific neurocognitive research originating in the Soviet Military and then continued in public research in the West such as Dr. Serge Kernbach at University of Stuttgart and Dr. Michael Persinger of Laurentian University.  This research is alo within the US Military Defense industry and hence is usually classified.  

It is based on the utilization of the Ahronov-Bohm effect, creating a potential energy shield to guard against cyberbased attacks on hardware and software. It protects the user from invasive electro-magnetic frequencies, effectively scrambling them before reaching the target vector, for instance the Microtubules of the Neurons in the Brain.   

The frequency_driver.ino is a Arduino Sketch file designed for use with the Ahronov-Bohm coil a piece of the Ahronov-Bohm generator created by Dr. Hal Puthoff. It generates totally random frequencies.  I prefer the accelerate_frequency_driver.ino it sets 4 random frequencies (salts) before a repeating pattern of accelerating EM waves forms.

<b>Threat Analysis:</b>


Since the end of World War I, the study of EM and Gravitational Waves for the purpose of information warfare (McCarron, 2021) has been persued by global strategic players such as the Nazi Regime in Germany, the USSR, and NATO alliance, while also persued by the Peoples Republic of China (PRC), while keeping in mind the only country not to ratify treaties banning biological weapons with the technical resources to do it, is Israel, which also has a history of conducting espionage against allies like the United States and has recruited many ex-Soviet engineers and is a society based in ethno-religious supramecy.  State actors are not the only ones that could have this capability as it is available on the black market, as well as any small technically outfitted terrorist group could also accomplish this technology. Indeed, the roots of political deception are found in the intoxication tactics of the 4th Reich inspired Black International. A full review of information warfare using signals and cybernetics is covered in McCarron 2021. 
 
The threat of using EM and Gravitoelectromagnetic weapons, of which Ahronov-Bohm (A-B) effect is a party to, was encountered primarily in the 1980s in the USSR. Soviet military-industrial research focused on 'remote biological effects' or remote (non-local, entanglement) influencing using A-B generators designed initially by Akhimov (Kernbach, 2017) around 1986 at least.  Later his research associate A V Bobrov experimented with using LEDs with modulated pulsed rhythms for the same purpose.  Previous to this Soviet research also focused on using gravitational waves for the purposes of non-local influence, possibly also involving the proposed Gravitational Ahronov-Bohm effect. After the fall of the Soviet Union Soviet researchers were brought to the west to be debriefed, for instance Okhtarin was interviewed by the CIA regarding his research into remote influencing using the Ahronov-Bohm effect (McCarron, 2021). In western parlance remote influencing is known as 'remote action'. When the Russians came west they were employeed by Lockheed-Martin to collaborate with their engineers, such as Dr. John Norseen who invented 'Bio-Fusion' and 'Thought-Injection' technology based on previous Soviet inventions. It is also worth noting that this technology is available on the black market according to Dr. Kernbach.  Incidents in the Soviet Union targeting the US Embassy using this technology are well documented (McCarron, 2021).  And recently the Havana US Embassy incident implicated the use of remote influencing technology as the source of the medical problems encountered by embassy staff. Additionally, former US military personnel are complaining of receiving the same remote influencing effects as that as the Embassy staff.
    
    
The scientific literature on the weaponization for the purposes of cyber attack are well established, although primarily only in Russian academic journals and languages. While Krishnan (2017) did not find evidence for their reality the Havana incident scientifically has documented the effect, and it's use as a weapon. Western academics have provided research and experimental data establishing it's validity.  The Persinger Group of Laurentian University, a pariochial school in Sudbury, Ontario has conducted numerous experiments showing that remote influencing is well founded in scientific theory.  Their work is also confirmed by the finding of Dr. Serge Kernbach at the University of Stuttgart, who is a Russian professor of cybernetics, the association of remote biological influence and cybernetics in Russia is a intertwined reaility.
    
    
    
Therefore, based on western academic research (Persinger et al), countermeasures are needed to counter such a threat.  No weapons is ever developed that the engineers do not also have their own countermeasures for.  The research into the A-B tech used by the Soviets by Hal Puthoff, formerly of Stanford Research Institute, reversed engineered the Akhimov Generators.  The work of Persinger et al, expanded on this reverse engineering, ultimately showing that the coils from the Puthoff Generator were all that was necessary for experiments documenting their ability to use angular momentum for entanglement as well as create a masking field to counter remote influencing (Persinger, Roll et al 2002).  This particular countermeasure is valid for the interference with remote waves, that is non-local field waves from a remote source, not in the local field where optical devices could be used as an attack vector (red team) on the visual cortex through the cavity resonators in the retinas.  The production of the coils is given below.  Persinger et al and Kernbach et al have provided detailed information on how to construct A-B generators, the coils used in this experiment are from Lehman et al (2015).  See 'Physics' section below for a deeper explanation to the A-B effect, Angular Momentum and Deep Correlations. 




<b>Coil Construction and Arduino Board Setup</b>


Parts list:
1. Arduino Uno Board, plus necessary connectors (purchase a starter kit online) 
2. a 10" Embroider Hoop (remove all metal)
3. Electric Tape
4. Laptop
5. Single strand 16 gauge speaker wire (low impedance we are dealing with nano Tesla here)
6. Arduino Breadboard
7. 1K Ohm Resistor
8. TIP120 to 220 Voltage Regulator
9. Diode
10. Blue LED (470nm Wavelength) 


Step 1: Make a Coil, see NRG Deep Correlation Video: https://www.youtube.com/watch?v=ygCqykp6tC4&t=5s

Step 2: Wire up the Arduino and Breadboard 
place the breadboard in front of you, and the Arduino board above the Breadboard with the power connector (connects to laptop usb) to the left. (see video https://www.youtube.com/watch?v=iRq9ksZmrQc&t=3s )

1. connect LED to pin 21 and 22
2. on the Arduino Uno out pin 9 to pin 21 infront right leg of LED. Connet gound pin 9 to Breadboard - negative base. 
3. Take 1K Ohm Resistor and connect to pin 22 inf front of LED short leg, connect resistor out to pin 20 in front of 120 TIP V regulator.
4. Voltage regulator, facing properly (see video) metal hole mount to rear, pace in pin 20,19,18
5. Ground regulator (red wire from regulator out 19, place in front)
6. In to coil, pin 19 in front of V regulator pin 19
7. Diode, (grey strip is out) grey end into + positive of breadboard base. In goes to pin 19 behind out to coil. (see video) 
8. Coil out to negative on board base.
    
Step 3: open accelerate_frequency.ino into Arduino LED then upload to Arduino Board.
    
Step 4: Place coil around object to shield from remote waves. 

NRG Excess Correlation Coil and Arduino Board Instructions: https://www.youtube.com/watch?v=MOlmLWQAIqI



Are Changing Angular Velocity Magnetic Fields a Countermeasure to Havana Syndrome and other Pulsed Modulated Frequency Cyberattacks?
By Michael. J. McCarron, 2021 (independent cybersecurity consultant, macciarain@protonmail.com)

Medical Pathology of Non-Local Weapons

     In the following I provide documentation on the physics of Ahronov-Bohm Effect (potential energy) weapons technology and neurological effects from these physics as it interacts with the interferometer known as the human brain.  The physiology of those attacked by RF based weapons in the US Embassy in Havana provides one of the first efforts at medically studying the use of directed waves against a human target.  After this I go into the use of entanglement and the physics of entanglement focusing on angular momentum and the utilization of the Ahronov-Bohm effect, including it’s Gravitational corollary to the EM version, covering also gravito-electromagnetism- the coupling of gravity and EM, which produces photon emmissions which is suggested by some researchers as that along with gravitons is posited as the boson involved in entanglement or deep correlations which is the physical basis of these weapons. Then I show that this work was begun in the Soviet Union and then transferred to the defense industry of the United States of America as well as other NATO members. After showing the neurological effects, then understanding the science behind the technology we can then correlate studies on A-B effect regarding Neurological effects to specific areas of the Brain affected in terms of functionality as studied by fMRI and QEEG by the Persinger Group cross correlated to changes studied in the Havana Syndrome medical studies.   

I. Profiling a Directed Energy Attack Medically Speaking
 
Havana Syndrome
Havana Syndrome is a popular term coined to refer to the illnesses experienced by diplomats at the US Embassy in Havana, Cuba in 2016. It is similar to incidents at the Moscow US Embassy of 2.4-4.0Ghz from 1953 to 1976. Another incident was reported in Guangzhou, China also at a US Embassy in 2018. The same illnesses were reported by Russian politician Boris Yeltsin (Kernbach, 2017) in the early 1990s during the break up of the Soviet Union and attempted coup by Communist Generals. Scientists studying the phenomenon cite microwaves as the culprit, directed pulsed Radio Frequency weapons. Whereas critics dismiss the use of highly sensitive technology to militaries around the world calling the situation a case of mass psychogenic illness, which fits well with a disinformation campaign to keep highly classified technology top secret.
    Neurologists at the University of Pennsylvania (Verma et al, 2019) studied the brains of embassy staff from the Havana incidents.  All professional diplomats and military personnel who complained of the following symptoms: 


Hearing strange grating noises, headache, hearing loss, memory loss, and nausea
Balance problems, tinnitus


Verma (2019) Neuroimaging studies focused on the change in white matter and grey matter volumes of the attacked individuals compared to controls the main area affected was the right hemisphere, specifically altering the auditory (BA 22)  and visual-spatial subnets (BA 17). Finding a difference of whole brain white matter volume, regional grey and white matter volume, mainly in the right hemisphere. The Cerebellar tissue micro-structural integrity was damaged. Functional connectivity in the auditory/visual-spatial subnets was reduced.  The study does not address a specific causality although they do believe that some of form of pulsed directed microwaves were involved. The researchers note that: “the clinical importance of these differences is uncertain and may require further study.” (Verma et al, 2019)  As shall be seen later the areas of BA 22 and 17 were involved in early Soviet and later Russian research as well as those scientist collaboration with western companies such as Lockheed-Martin (see Norseen et al, 1999). An additional area affected was the volume differences between right and left ventral diencephalon, the caudal (posterior) part of the forebrain containing the thalamus, hypothalamus and ventral thalamus and the third ventricle. Further, they found higher mean fractional anisotropy, the property of substances to exhibit variations in physical properties along different molecular axes (i.e. crystals, H2O). 
    In the supplementary information provided in their study Table 7 provides some of the areas of the brain that have high levels of differentiation from the control group.

Brain organelles with large difference from normative values of brain morphology:
    Cuneus, receives visual information from the senses, retina. Broadmann Area 17.  

   Anterior Insula, involved in consciousness, salience, emotion, homeostasis, compassion/empathy, taste, perception, self-awareness, cognitive function interpersonal experience-- involved in psychopathology, connects to the Amygdala. Loss of Balance and vertigo in people with lesions in the insula.  The posterior insula processes auditory detection, simple auditory hallucinations were elicited by electrical functional stimulation. It has no Broadmann area as it covers a large area. 2 Spontaneous activity fluctuations in anterior insular cortex influence auditory perception (Sterzer, 2010)

    Putamen, Broadman Area 8, regulate movements at various stages (preparation , execution and influences learning.  Neurotransmitters GABA, acetylcholine, encaphalin, dopamine. It receives serotonin, glutamate. It is part of the “hate circuit” along with the insula . In Male-to-Female Trans people this area has significantly larger grey matter. 

    Post-Central Gyrus, Broadmann Area 1,2,3. Somatasensory cortex, part of Default Network, contains a sensory strip representing the lower part of the body, contains an inverted map of the contralateral body mirroring the motor strip.  Senses touch, pressure, pain, temperature. TMS improves tactile discrimination and reorganizes the somatasensory map, also affects pain modulation. 

    Middle Temporal Gyrus (BA 21, part of Temporal Lobe: BA 20,21,22, measured by EEG C4)  Functions for object vision, recognition, facial recognition. 

    Triangular part of the Inferior Frontal Gyrus (BA 45, part of Broca’s Area as cited by Norseen), part of the IFG: BA 44,45,47  Semantic processing, associated with N400 waves in EEG. Part of the VLPFC [related to hypnosis, (McCarron 2021)]. Functions as cogntive control of memory.  Language processing. In Schizophrenics this area is distorted. 

    Parietal Operculum Broadmann Area 40 secondary somotasensory system Recent data suggest that the parietal operculum acts as an integration center within a multimodal network, originating from different primary sensory and motor cortices and projecting to frontal, parietal and temporal cortical hubs, which in turn govern cognitive and motor functions. Thus, parietal operculum might also play a crucial role in the integrated control of voluntary movement and posture. (Marchese, 2019) 
    Supramarginal Gyrus The supramarginal gyrus is part of the somatosensory association cortex, which interprets tactile sensory data and is involved in perception of space and limbs location. It is also involved in identifying postures and gestures of other people and is thus a part of the mirror neuron system.  Broadmann Area 40

    Temporal Pole found in the Temporal Lobe complex. The temporal pole is a paralimbic region involved in high level semantic representation and socio-emotional processing. The uncinate fasciculus provides a direct bidirectional path to the orbitofrontal cortex, allowing mnemonic representations stored in the temporal pole to bias decision making in the frontal lobe. Broadmann Area 38

Below where I present the data on the Brain science involved in studying the affects of A-B weapons we will see how the Havana Study correlates with Persinger et als research. Another researcher on A-B weapons is Dr. Serge Kernbach at U. Stuttgart. He remarks specifically on the Havana Syndrome in relation to weapons:

Can such neurological symptoms occur when the rhythms of biochemical oscillators in the central nervous system are disturbed during nonlocal exposure for several weeks or months? Specialists should answer these questions. (Kernbach, 2017)

The Verma et al study is one attempt to answer this question. He further goes into the Soviet military developers view of these technologies as non-lethal weapons.

Akimov spoke about the possibility of using this technology in a kind of non-lethal weapon (for example, and at the conference ’KGB: Yesterday, Today, Tomorrow’ [29]). Taking into account that this experiment is easy to repeat (for example, the script for creating feedback in the ’transmitter’ is provided in the paper), we ask ourselves, whether the ’1986 experiment’ did open the Pandora’s box for nonlocal biological technologies? 
    An unexpected result of this replication experiment represents the potential possibility for a remote monitoring of biological organisms (and possibly non-biological objects). By introducing nonlocal feedback, the object on the transmitter side becomes ’entangled’ with the receiver and can thus be nonlocally monitored. It is necessary to set up such an operation of a remote station, which would not affect the monitoring object. This new aspect needs further verification and development. (Kernbach, 2017)

It was the Soviet developers that used the quantum mechanical effect of entanglement to “dose” a target of their technology using the Ahronov-Bohm effect.  The creation of the actual tech is well documented and it’s transition into the west, including defense industry markets as well as being available in the black market to non-state actors, so that in our day anyone from a state to a private defense contractor (such as SCL Group with Cambridge Analytica), as well as terrorist organization of all styles of the political spectrum with sufficient small-scale technical infrastructure.


Soviet Technology in the US National Security Defense Industry
    I cover the history and development of Soviet Military technology and it’s transfer to the United States of America in my book Battlespace of Mind (McCarron 2021)  (http://www.github.com/autonomous019/Battlespace_Of_Mind). A succinct account is that the development of A-B weapons actually predates that of the Cold War, with early work begun in this area in the 1920s during the Reichswehr-Soviet Technical cooperation agreement, the Rapahoe Agreement.  In the 1930s Nazi researchers according to Soviet researchers developed the use of remote influencing biological objects with equipment seized during the end of the war, initially begun by Argonne. Later, the Soviets arrested key nuclear engineers of the Nazi regime and brought them under forced labor to aid the Soviet Nuclear program.  Earlier work had been done during the war, including the awareness of viscosity of deuterium under studying D2O. A secret weapons development intelligence bureau was set up in Berlin during the war that involved one of the founders of Quantum Mechanics, Pascual Jordan, and one of his close collaborators in molecular biology and the Nazi Nuclear program was taken to the Soviet Union.  Russian researchers trace the origins of the Cold War weapons program which was re-started in the 1950s after Stalin stopped all research in 1937, purging his military just before the war and diagnosed with schizophrenia which can also mimic temporal lobe epilepsy which also as we shall see below match symptoms of A-B effect on the Brain when used maliciously. 
    Reflexive Control, Cybernetics and Biology where used to further the weapons program.  In the later part of the 1990s the US NSA became interested in Soviet Weapons development using A-B Effect and specifically at injecting ‘corrective behavior’ using various psychological mechanism delivered remotely through the transmitters of the A-B Generators.  One company contracted to develop American versions of Soviet technology was Lockheed-Martin, which is where an engineer, Dr. John Norseen, who studied in Russia, was contracted to develop Air Control systems which involved interactions monitored automatically as a means to assist the pilot for safety purposes.  His other work with Lockheed-Martin involved the creation of sentient machines (Norseen, 2000) for automation, the creation of ‘Thought-Injection’ to correct the behavior of terrorists. His ideals of using ‘Thought-Injection’ were reported in popular publications as well as military publications of the late 1990s and early 2000s, before talk of this work stopped.  We are aware of his work by his public statements, papers and conversations with others that were documented such as (Laurie, 2002).  From these open public sources we can gain valuable information on how a neurological based weapon would be created. 

    The following is different material from that presented in McCarron 2021 (Ch.4 ‘Lessons from an American Weapons Developer’). Here I drill down into some of the specific areas that Norseen was interested in, in terms of ‘Thought-Injection’ in which he proposed using radar to inject and monitor the thoughts of the terrorist, his neurobiological interests primarily focused on using Electromagnetism (E x H Fields), to influence the Microtubules (MT10 and MT13 types) in the Neurons of the Brain, which was compiled from Brain Maps using QEEG working with Soviet Researcher Juri Kropotov of the Brain Institute in St. Petersburg one of the original centers of research for remote influence in terms of psychology. He coined the term BioFusion as on overarching term relating to the sensor fusion of the human senses. In a 1999 study co-authored between Norseen and Kropotov studied the visual cortex, one of the main areas affected by the Havana Syndrome, specifically in Norseen’s other work (Norseen, 2000) he cites specifically BA 17,18 which is the visual pathway, BioFusion as the sensory input is the starting point in understanding how ‘Thought-Injection’ is accomplished.  Norseen has remarked on what is BioFusion: “emergent process of biochemical induced, electromagnetic E & H [electric and magnetic flux] fields mediated interactions of information with uniquely configured neural structures, and expressed into work via protein reconfiguration [microtubules] under the term BioFusion.” (Norseen, 2000) and “Biofusion involves posterior inferior temporal gyri (ITG) in visual perception modality. The ability to blend vision and verbal modality in the Temporal Cortex, TC-22 and Broadmann’s Area 44 [Broca’s Area].” (Norseen, 2000). It is interesting that the areas targeted are also areas that were affected by Havana Syndrome.  The ability to sense and alter a brain state happens in the microsecond scale, see point durations below, as explained by Norseen:

“The time scale for BioFusion action is remarkably short.  The vast majority of the brain executes its portfolio of actions in seconds to tenths, to hundredths of seconds.  It is very hard for the brain consciously to concentrate for minutes or hours on end, almost as if in the striatum, our sense of time to dwell, our biochronicity is preset for the sub-second regime.  Can this be reset?  The answer would appear to be yes, if only at least from episodic documentary from periods of altered states and periods of time loss due to dissociative or fugue events.  This also does not preclude that the brain may be engaged in very long term, but non-conscious, mathematical processing.  So what would happen if suddenly, instantly, in fit of advanced, catastrophic evolutionary rage, that our brain would suddenly operate on a far more distant Time Slope of not seconds and partial seconds, but thought domains of hours, days, years – allowing Sentient Machines to handle the routine reasoning tasks of the lesser Time Limits?  Such time-thought testing is now available in Cortical Emulation Research (CER).  And where is the dark matter of the brain, the untapped regions that will provide for our future, perhaps even Accelerated Rates of Evolution?  The answer may exist at the layer in the anterior cingulate between the older brain, deeper brain and the outer folding top cover of the cortex, as well as in the less knotty, less complicated realm of the right side of the brain – ‘The God Spots!”” (Norseen, 2000)

It is interesting to note that Norseen specifically mentions the anterior cingulate which is a prime difference between highly and non-highly hypnotizable persons who have an enlarged ACC by grey matter volume, He also mentions in other places the connection to the Amygdala, which is enlarged in highly hypnotizables and in Epileptic patients. The Cortical Emulation Research he is referencing is that of former Soviet Dr. Juri Kropotov.  The timings involved come into play in creating modulated phases or frequencies which are used to alter the electromagnetism of the brain.  As shall be seen is the main principle involved in the Soviet A-B Generators.   Norseen speaks of magnetism and reconfiguration of proteins, like the Microtubules:

“emergent process of biochemical induced, electromagnetic E & H [electric and magnetic flux] fields mediated interactions of information with uniquely configured neural structures, and expressed into work via protein reconfiguration under the term BioFusion.” (Norseen, 2000)

    Sentient Machines of which Dr. Norseen advocates, which is a common attribute of being interested in cybernetics along with remote influence of biological objects, seen routinely in Soviet research as well as by Dr. Serge Kernbach who teaches Cybernetics, reminding us that cybernetics is the study of control in the machine and the animal. The primary protein that Dr. Norseen is interested in altering using EM waves is that of the MT10 and MT13 structures in the neurons. In some of his presentation slides (see Laurie 2002) he writes of MT10 as an electrical biocomputer, and importantly for A-B effect MT13 as a magnetic biocomputation, which he notes is targeted by potentials as in the A-B Effect. Pribram speaks of MT as a wave guide, “The intracellular spread of dendritic polarizations can be accounted for by microtubular structures that act as wave guides and provide additional surface upon which the polarizations can act” (Pribram, 1999) Norseen posited the concept of Quanum Shift Keys (QSK) which interacts as a lock-key mechanism to alter MTs.  He cites in his work the ideals of Primbram and Hameroff, who also worked with former Communist block scientist Dr. Koruga (U. of Belgrade, Serbia, former Yugoslavia), on the ideal of Microtubules and Consciousness, Hameroff published with Karl Pribram on the topic in 1994. Brain Holography was the area cited in term sof Pribram as we shall see below, the ideals of MTs and neurons goes back to the concept of the Objective Reduction a gravitational collapse of the wave state created by Penrose and Hameroff, here we see already the role of gravity and gravitons in the collapse as shall be discussed later in relation to the Gravitational Ahronov-Bohm effect and other Soviet research in control using gravitational waves, (See McCarron 2021, ‘Quantum Consciousness’).  The orchestrated reduction according to Norseen takes place in the Neuropil and involves 4 Quanta, a quaternion.   Norseen writes regarding the role of QSK and MTs: 

“...a biofield communication both local and non-local to the protein MT strings. Calpain induced start/stop in the dendritic-synaptic receptors, with varying degrees of glial cells neurochemical nutrient infusion, turn on or off the QSK coded learning sequences in the MT.” (Norseen, 1996). 

The role of magnetic fields in interstitial water of MTs has been proven by Bandyopadhyay’s Group in The Materials Science Institute in Japan. We see that the QSK is a E-H Field as mentioned by Norseen. It is claimed that human thought can be reduced down to a Krylov sub-space, ““the human condition captured in automated krylov space”, as Norseen put it (Norseen, 2000).  These calculations were begun by Juri Kropotov in the Soviet Union in the 1980s.  Again, it does not seem Norseen has invented these techniques but learned of them for Lockheed-Martin from the original Soviet Communist science researchers, Kropotov has called the collapse of the totalitarian-dictatorship of the Soviet Union ‘horrible’ (Kropotov, 2009).  Norseen writes regarding Kropotov’s contribution to ‘Thought-Injection’:

Even more extraordinary, Dr. Kropotov was able to capture the complex adaptive rules of mental functions, perceptual activity across sensory modalities, into software to produce Cortical Emulation Research, by which the same math functions that appear in brains, can now be made to emerge in software.  This finding of extreme importance leads us to Information Injection via the introduction or playback of the Inverse Function of the Gabor in Hilbert Space, or whatever other mathematical domain that also may be workable in various species’ brains. Thoughts then could be categorized as either culturally dependent, or when synthetically produced, as culturally independent.  Both culturally independent and dependent thought means that machines could be produced that could conceivably never be able to communicate with a human.  It/they would exist in its/their own perceptual world made up of its/their own mathematical thought structures.  But more likely is that some common, semiotic language of human-machine interests will arise that can universally transform to some degree each particular species, to include synthetic species, into emergent mathematical thought domains.” (Norseen, 2000) 
Dr. Kropotov is a world renownded scientist in what has become known as Quantitative Electroencephalography (QEEG), he worked extensively studying various medical conditions of the Brain using EEG measuring tools, fMRI, during the late Soviet days Positron Electro Tomography to map the various parts of the brain and their functions.  However, when the ‘horrible’ collapse of the Soviet Union came he found himself, like many scientists who went to the west for employment, working with Karl Pribram in the early 1990s at Radford University.  So we can understand the synthesis of the quantitative methods of Kropotov and those of the holographic brain of Karl Pribram reflected in the writings of John Norseen, a collaborator of Kropotovs.  As mentioned previously, one of the main areas of influence are the visual cortex (BA 17,18) in Thought Injection to be delivered via em waves, this is also the one of the primary areas showing differential measurements in GM and WM in the fMRIs of staff affected by Havana Syndrome, see below. Kropotov and Norseen collaborated on a paper in 1999, Norseen lists himself as Lockheed-Martin and uses his work address in this paper.  Kropotov previously had come up with the Canonical Cortical Module (CCM), which is a way of dividing the brain into a matrix of 500x500 individual modules, each matrix or module representing functionality in the cortical area of the brain.  It is reminiscent of the AI technique Convolutional Neural Networks.  In the maths of the CCM Operators include encoding all orientations and all possible spatial frequencies which are extracted in the cortical area at a given eccentricity (Norseen & Kropotov, 1999) 
    Another trade craft gleaned from Norseen’s collaboration with Kropotov was that of the use of the Gabor Function, a sinusoid wave windowed with a Gaussian wave where frequency and orientation as well as size of the function can be tuned, Norseen credits his use of the Gabor Function and the Inverse transform at 14Hz to Kropotov (Laurie, 2002), who again worked with Pribram, who comments on Gabor functions:

During the 1970's it became apparent that Gabor's notation also applied to
the cerebral cortical aspect of visual and somatic sensory processing. The most
elegant work was done with regard to the visual system. A recent review by Tai
Singe Lee [2] in the IEEE casts these advances in terms of 2D Gabor wavelets
and indicates the importance of frames and specifies them for different sampling
schemes. For the monkey, the physiological evidence indicates that the
sampling density of the visual cortical receptive fields for orientation and frequency
provides a tight frame representation through oversampling.
     The 2D Gabor function achieves the resolution limit only in its complex
form. Pollen and Ronner did find quadriture phase [Norseen’s 4 Quanta?] (even-symmetric cosine and odd-symmetric sine) pairs of visual receptive fields. (Pribram, 1999)

The Gabor function is used to gather texture or fine detail of object recognition. In another presentation slide Norseen cites the use of hyper spectral analysis, fine detail analysis of spectral lines, which is also preluded by the work of former military researcher Shkatov in using A-B effect techniques in sensing, Since 2000 they used the method ‘torsion [AB] phase portrait’ (TPP), торсионного фазового портрета (ТФП)) for remote fine field diagnostics. (Shkatov 2009), claiming to glean potential energy sources from EM based media. 

. Norseen writes about the use of Gabor-Like Functions in Hilbert Space (a dimensional space of at least 3d):

“Hence, to find a Gabor-Like Function in Hilbert Space as the operant mathematical operation where neural structure interacts with information compressing it from the environment would be the precise math structure that one could use to define the exact moment when Perception occurs from the general state input from or of the Sensory Modalities.  A specific gabor function could then be assigned to each object perceived in the brain.  A data base could be built up, a thought code of mathematical expressions that literally is what the brain actually sees when information, like a bernoulli’s code, passes through neural structure.  Just as wind under an airfoil produces lift, a gabor function is the moment when information entering neural structure creates a thought.  Such a ‘Eureka’ moment was discovered in Pavlov’s Laboratory in 1996, by Dr. Juri Kropotov and his team.  They found that just as Pribram predicted, when you look at neural structure interacting with signal to noise information from the external environment, that a Gabor-Like Function in Hilbert Space emerges at the exact moment of perception from the sensory field.  Based on the work described in this paper, BioFusion R&D findings strongly suggest earlier predictions that human brain perceptual processes represent, at a minimum, an n-dimensional family of interacting Gabor-Like Functions in Hilbert Space (Pribram-91).” (norseen, 2000)

The mathematical representation of human thought for the purposes of sensory fusion enables a cognitive map to be produced. Norseen speaks of the key ability to capture brain em maps as well as send back via an inverse function either the same or altered information to the brain. He speaks of deceiving the mind to accept these thoughts as one’s own, this concept of a A-B Effect injected thoughts not being perceived as alien to one’s own thought train is written of by the Persinger Group as well.  Norseen comments on inverse function or injection:

“[to die inject thoughts] in order to fool the brain into accepting it as real. And this inverse injection must also very closely model the exact E and H fields, the EMF shapes that the original Gabor like Function in Hilbert Space” (McCarron 2021, Lessons from an American Weps designer)” 

The connection between EM waves and the ability to alter Hilbert Space is very explicit in the above. The wave patterns injected or QSK of EM waves is directly connected to entanglement or deep correlations by Norseen, the A-B Generators are also based on entanglement, He remarks:  

‘QSK originates in the Orchestrated Reduction of Quantum entanglement at specific EM resonating frequency locations in the protein microtubulin in the neuropil. QSK is then communicated via oscillating and standing waves [solitons] in the neurosynaptic-dendritic region… At certain frequency and energy threshold a combining resonance is established in the brain function that binds the various oscillating brain subresonances into a cohesive sentient pattern.” (Norseen, 2000)

Cognitive recall is comprised of Gabor Functions in Hilbert Space. The MTs are altered by the magnetic fields of interstitial (within the protein) waters. The wave form specifically targets calpain as Norseen points out: “EM Resonance, then calpain (neuromolecule), then calpain dissipates and a structural imprint of the QSK encoded wave-front interference pattern onto protein [MT] structure.” (Laurie, 2002)

Pribram has explained the connection of magnetic fields to neurons in the following:
 
To account for these properties we turn to the dendritic membrane and its
immediate surround. Dendritic membranes are composed of two oppositely
oriented phospholipid molecules. The interior of the membrane is hydrophobic
as it formed by "lipids which form a fluid matrix within which protein molecules
are embedded - the lipids can move laterally at rates of 2 ~sec; protein
molecules move about 40 times more slowly (50 nm/sec or 3 ~tm/min)" ([7], p.
44). Some of the intrinsic membrane proteins provide channels for ion movement
across the membrane.

we proposed that a perimembranous process occurs within dendritic compartments during which boson condensation produces a dynamically ordered state in water.

We have gone on to speculate that as each pattern of signals exciting the
dendritic arborization produces a macroscopic, ionically produced change of
the charge distribution in the dendritic network, it triggers a spontaneous
symmetry breaking of a radiation field (a boson condensation) altering the
water molecular field in the immediately adjacent perimembranous region. A
macroscopic domain of the dynamically ordered structure of water is created in
which the electric dipole density is aligned in one and the same direction. It is
this domain of dynamically ordered water that is postulated to provide the
physical substrate of the interactions among polarizations occurring in dendritic
spines.


To summarize neurons are controlled by the electro-magnetic waves that interact with the Microtubules, these microtubules using QSK can be programmed and altered as well as read out using various spectroscopy.







<b>Works Cited:</b>

 Chiao, R. various papers on gravitational poynting vector. 
		-  (2002) Superconductors as quantum transducers and antennas for gravitational and 			electromagnetic radiation 
		- Gravitational Ahronov Bohm Effect and its Connection to Parametric Oscillators and 			Gravitational Radiation (2013)
		- Dynamical Casimir Effect and the Possibility of laser-like generation of Gravitational 			Radiation (2017)

Fickler, R., Lapkiewicz, R., Plick, W.N., Krenn, M., Schaeff, C., Ramelow, S. and Zeilinger, A. (2012) Quantum Entanglement of High Angular Momenta. Science, 338, 640-643. http://dx.doi.org/10.1126/science.1227193

Gosh. Subrata, Fujita, Daisuke (2014) Live Visualizations of Single Isolated tubulin Protein Self-Assembly via tunneling current: Effect of electromagnetic pumping during spontaneous groth of microtubule 

Hu, H. & Wu. M. (2006) Evidence of Non-local Chemical, Thermal and Gravitational Effects . http://cogprints.org/5613, http://arxiv.org/ags/quant-ph/0208068v4, NeruoQuantology, 2006; 4: 2901-306.

S. A. Koren, M. A. Persinger (2002) Possible Disruption of Remote Viewing by Complex Weak Magnetic Fields around the Stimulus Site and the Possibility of Accessing Real Phase Space: A Pilot Study
First Published December 1, 2002 Research Article Find in PubMed
https://doi.org/10.2466/pms.2002.95.3.989

Kernbach, Serge (2017) Tests of the circular Poynting vector emitter in static E/H fields
International Journal of Unconventional Science
Issue E2, pp. 23-40, 2017 http://www.unconv-science.org/e2/kernbach1
Association of Unconventional Science, 2017

Kernbach, Serge (2018) Replication experiment on distant influence on biological organisms conducted in 1986, IJUS, Issue E2, pages 41-46, 2018 http://www.unconv-science.org/pdf/e2/kernbach2-en.pdf

 Kernbach, S. (2016) On metrology of systems operating with ‘high-penetrating’ emmision IJUS E1
 
 Kernbach, S. Distant Monitoring of Entangled Macro-Objects NeuroQuantology | March 2019| Volume 17 | Issue 03 | Page 19-42| doi: 10.14704/nq.2019.17.03.1977


Murugan, N., Karbowski, L. Dotta, B., Persinger, M. (2015) Delayed Shifts in pH Responses to Weak Acids in Spring Water Exposed to Circular Rotating Magnetic Fields: A Narrow Band Intensity-Dependence
January 2015International Research Journal of Pure and Applied Chemistry 5(2):131-139
DOI: 10.9734/IRJPAC/2015/13156 https://www.researchgate.net/publication/282624530_Delayed_Shifts_in_pH_Responses_to_Weak_Acids_in_Spring_Water_Exposed_to_Circular_Rotating_Magnetic_Fields_A_Narrow_Band_Intensity-Dependence

Lehman, B., Scott, M. Rouleau, N., Tessaro, L. (2015) Experimental Production of Excess Correlation across the Atlantic Ocean of Right Hemispheric Theta-Gamma Power Between Subject Pairs Sharing Circumcerebral Rotating Magnetic Fields (Part II)
September 2015 https://www.researchgate.net/publication/282661047_Experimental_Production_of_Excess_Correlation_across_the_Atlantic_Ocean_of_Right_Hemispheric_Theta-Gamma_Power_Between_Subject_Pairs_Sharing_Circumcerebral_Rotating_Magnetic_Fields_Part_II
see video presentation at Consciousness Hacking: https://www.youtube.com/watch?v=L5I3wOyo-rg

Komal Saxena, Pushpendra Singh, Pathik Sahoo, Satyajit Sahu, Subrata Ghosh, Kanad Ray, Daisuke Fujita, Anirban Bandyopadhyay. Fractal, Scale Free Electromagnetic Resonance of a Single Brain Extracted Microtubule Nanowire, a Single Tubulin Protein and a Single Neuron. Fractal and Fractional. 4 [2] (2020) https://doi.org/10.3390/fractalfract4020011

Norseen, J. Kropotov, J. (1999) Bio-fusion for intelligent systems control
John D. Norseen, Juri D. Kropotov, Inna Z. Kremen
Author Affiliations +
Proceedings Volume 3719, Sensor Fusion: Architectures, Algorithms, and Applications III; (1999) https://doi.org/10.1117/12.341364
Event: AeroSense '99, 1999, Orlando, FL, United States

Norseen, John (1996) Images of Mind: The Semiotic Alphabet, http://www.acsa2000.net/john2.html 

Norseen, John Mathematics, BioFusion and Reflexive Control for Sentient Machines, Presentation for International Reflexive Control Symposium(RC’2000) Russian Academy of Sciences – Institute for Psychology 17 – 19 October 2000     Moscow, Russia


Persinger Group Direct Experiments

    • Dotta, B.T. and Persinger, M.A. (2012) “Doubling” of Local Photon Emissions When Two Simultaneous, Spatially- Separated, Chemiluminescent Reactions Share the Same Magnetic Field Configurations. Journal of Biophysical Chemistry, 3, 72. http://dx.doi.org/10.4236/jbpc.2012.31009

    • Dotta, B.T., Murugan, N.J., Karbowski, L.M. and Persinger, M.A. (2013) Excessive Correlated Shifts in pH within Distal Solutions Sharing Phase-Uncoupled Angular Accelerating Magnetic Fields: Macro-Entanglement and Information Transfer. International Journal of Physical Sciences, 8, 1783-1787.

    • Dotta, B.T., Karbowski, L.M., Murugan, N.J. and Persinger, M.A. (2013) Incremental Shifts in pH Spring Water Can Be Stored as “Space-Memory”: Encoding and Retrieval through the Application of the Same Rotating Magnetic Field. NeuroQuantology, 11. http://dx.doi.org/10.14704/nq.2013.11.4.714

    • Rouleau, N., Carniello, T.N. and Persinger, M.A. (2014) Non-Local pH Shifts and Shared Changing Angular Velocity Magnetic Fields: Discrete Energies and the Importance of Point Durations. Journal of Biophysical Chemistry. http://dx.doi.org/10.4236/jbpc.2014.52006

    • Rouleau, N. and Persinger, M. (2015) Local Electromagnetic Fields Exhibit Temporally Non-Linear, East-West Oriented 1 - 5 nT Diminishments within a Toroid: Empirical Measurement and Quantitative Solutions Indicating a Potential Mechanism for Excess Correlation. Journal of Electromagnetic Analysis and Applications, 7, 19-30. http://dx.doi.org/10.4236/jemaa.2015.72003

    • Scott, M.A., Rouleau, N., Lehman, B.S., Tessaro, L.W.E., Juden-Kelly, L.M. and Persinger, M.A. (2015) Experimental Production of Excess Correlation Across the Atlantic Ocean of Right Hemispheric Theta-Gamma Power between Subject Pairs Sharing Circumcerebral Rotating Magnetic Fields (Part II). Journal of Consciousness Research & Exploration, 6, 658-707.

    • Puthoff, H. (1998) US Patent 5845220 ‘Communication Method and Apparatus with Singals Comprising Scalar and Vector Petentials without Electromagnetic Fields [Ahronov-Bohm Generator]


Verma, R., et al (2019) Neuroimaging Findings in US Government Personnel With Possible Exposure to Directional Phenomena in Havana, CubaJAMA. 2019;322(4):336-347. doi:10.1001/jama.2019.9269

