inputData = 'data/CORELLI_145931.nxs.h5'

LoadEventNexus(Filename=inputData, OutputWorkspace='145931')

ConvertToMD(InputWorkspace='145931',
            QDimensions='Q3D',
            dEAnalysisMode='Elastic',
            Q3DFrames='Q_lab',
            LorentzCorrection=True,
            OutputWorkspace='145931_MD')

FindPeaksMD(InputWorkspace='145931_MD',
            PeakDistanceThreshold=0.5,
            DensityThresholdFactor=600,
            OutputWorkspace='145931_MD_Peaks',
            EdgePixels=3)

MaskPeaksWorkspace(InputWorkspace='145931',
                   InPeaksWorkspace='145931_MD_Peaks',
                   XMin=-4,
                   XMax=4,
                   YMin=-4,
                   YMax=4,
                   TOFMin=0,
                   TOFMax=300)
