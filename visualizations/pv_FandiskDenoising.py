# trace generated using paraview version 5.11.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()



# create a new 'Xdmf3ReaderS'
classicxdmf = Xdmf3ReaderS(registrationName='Classic.xdmf', FileName=[os.getcwd() + '/FandiskDenoising/Newton/output/Classic.xdmf'])
classicxdmf.PointArrays = ['f_105']
classicxdmf.CellArrays = []
classicxdmf.Sets = []

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# create a new 'PVD Reader'
fandisk_cleanpvd = PVDReader(registrationName='fandisk_clean.pvd', FileName= os.getcwd() + '/FandiskDenoising/fandisk_clean.pvd')
fandisk_cleanpvd.CellArrays = []
fandisk_cleanpvd.PointArrays = ['f_5']
fandisk_cleanpvd.ColumnArrays = []

# create a new 'PVD Reader'
fandisk_noisepvd = PVDReader(registrationName='fandisk_noise.pvd', FileName=os.getcwd() + '/FandiskDenoising/fandisk_noise.pvd')
fandisk_noisepvd.CellArrays = []
fandisk_noisepvd.PointArrays = ['f_5']
fandisk_noisepvd.ColumnArrays = []

# set active source
SetActiveSource(classicxdmf)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
classicxdmfDisplay = Show(classicxdmf, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
classicxdmfDisplay.Selection = None
classicxdmfDisplay.Representation = 'Surface'
classicxdmfDisplay.ColorArrayName = [None, '']
classicxdmfDisplay.LookupTable = None
classicxdmfDisplay.MapScalars = 1
classicxdmfDisplay.MultiComponentsMapping = 0
classicxdmfDisplay.InterpolateScalarsBeforeMapping = 1
classicxdmfDisplay.Opacity = 1.0
classicxdmfDisplay.PointSize = 2.0
classicxdmfDisplay.LineWidth = 1.0
classicxdmfDisplay.RenderLinesAsTubes = 0
classicxdmfDisplay.RenderPointsAsSpheres = 0
classicxdmfDisplay.Interpolation = 'Gouraud'
classicxdmfDisplay.Specular = 0.0
classicxdmfDisplay.SpecularColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.SpecularPower = 100.0
classicxdmfDisplay.Luminosity = 0.0
classicxdmfDisplay.Ambient = 0.0
classicxdmfDisplay.Diffuse = 1.0
classicxdmfDisplay.Roughness = 0.3
classicxdmfDisplay.Metallic = 0.0
classicxdmfDisplay.EdgeTint = [1.0, 1.0, 1.0]
classicxdmfDisplay.Anisotropy = 0.0
classicxdmfDisplay.AnisotropyRotation = 0.0
classicxdmfDisplay.BaseIOR = 1.5
classicxdmfDisplay.CoatStrength = 0.0
classicxdmfDisplay.CoatIOR = 2.0
classicxdmfDisplay.CoatRoughness = 0.0
classicxdmfDisplay.CoatColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.SelectTCoordArray = 'None'
classicxdmfDisplay.SelectNormalArray = 'None'
classicxdmfDisplay.SelectTangentArray = 'None'
classicxdmfDisplay.Texture = None
classicxdmfDisplay.RepeatTextures = 1
classicxdmfDisplay.InterpolateTextures = 0
classicxdmfDisplay.SeamlessU = 0
classicxdmfDisplay.SeamlessV = 0
classicxdmfDisplay.UseMipmapTextures = 0
classicxdmfDisplay.ShowTexturesOnBackface = 1
classicxdmfDisplay.BaseColorTexture = None
classicxdmfDisplay.NormalTexture = None
classicxdmfDisplay.NormalScale = 1.0
classicxdmfDisplay.CoatNormalTexture = None
classicxdmfDisplay.CoatNormalScale = 1.0
classicxdmfDisplay.MaterialTexture = None
classicxdmfDisplay.OcclusionStrength = 1.0
classicxdmfDisplay.AnisotropyTexture = None
classicxdmfDisplay.EmissiveTexture = None
classicxdmfDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
classicxdmfDisplay.FlipTextures = 0
classicxdmfDisplay.BackfaceRepresentation = 'Follow Frontface'
classicxdmfDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.BackfaceOpacity = 1.0
classicxdmfDisplay.Position = [0.0, 0.0, 0.0]
classicxdmfDisplay.Scale = [1.0, 1.0, 1.0]
classicxdmfDisplay.Orientation = [0.0, 0.0, 0.0]
classicxdmfDisplay.Origin = [0.0, 0.0, 0.0]
classicxdmfDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
classicxdmfDisplay.Pickable = 1
classicxdmfDisplay.Triangulate = 0
classicxdmfDisplay.UseShaderReplacements = 0
classicxdmfDisplay.ShaderReplacements = ''
classicxdmfDisplay.NonlinearSubdivisionLevel = 1
classicxdmfDisplay.UseDataPartitions = 0
classicxdmfDisplay.OSPRayUseScaleArray = 'All Approximate'
classicxdmfDisplay.OSPRayScaleArray = 'f_105'
classicxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
classicxdmfDisplay.OSPRayMaterial = 'None'
classicxdmfDisplay.BlockSelectors = ['/']
classicxdmfDisplay.BlockColors = []
classicxdmfDisplay.BlockOpacities = []
classicxdmfDisplay.Orient = 0
classicxdmfDisplay.OrientationMode = 'Direction'
classicxdmfDisplay.SelectOrientationVectors = 'f_105'
classicxdmfDisplay.Scaling = 0
classicxdmfDisplay.ScaleMode = 'No Data Scaling Off'
classicxdmfDisplay.ScaleFactor = 0.526055908203125
classicxdmfDisplay.SelectScaleArray = 'None'
classicxdmfDisplay.GlyphType = 'Arrow'
classicxdmfDisplay.UseGlyphTable = 0
classicxdmfDisplay.GlyphTableIndexArray = 'None'
classicxdmfDisplay.UseCompositeGlyphTable = 0
classicxdmfDisplay.UseGlyphCullingAndLOD = 0
classicxdmfDisplay.LODValues = []
classicxdmfDisplay.ColorByLODIndex = 0
classicxdmfDisplay.GaussianRadius = 0.02630279541015625
classicxdmfDisplay.ShaderPreset = 'Sphere'
classicxdmfDisplay.CustomTriangleScale = 3
classicxdmfDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
classicxdmfDisplay.Emissive = 0
classicxdmfDisplay.ScaleByArray = 0
classicxdmfDisplay.SetScaleArray = ['POINTS', 'f_105']
classicxdmfDisplay.ScaleArrayComponent = 'X'
classicxdmfDisplay.UseScaleFunction = 1
classicxdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
classicxdmfDisplay.OpacityByArray = 0
classicxdmfDisplay.OpacityArray = ['POINTS', 'f_105']
classicxdmfDisplay.OpacityArrayComponent = 'X'
classicxdmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
classicxdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
classicxdmfDisplay.SelectionCellLabelBold = 0
classicxdmfDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
classicxdmfDisplay.SelectionCellLabelFontFamily = 'Arial'
classicxdmfDisplay.SelectionCellLabelFontFile = ''
classicxdmfDisplay.SelectionCellLabelFontSize = 18
classicxdmfDisplay.SelectionCellLabelItalic = 0
classicxdmfDisplay.SelectionCellLabelJustification = 'Left'
classicxdmfDisplay.SelectionCellLabelOpacity = 1.0
classicxdmfDisplay.SelectionCellLabelShadow = 0
classicxdmfDisplay.SelectionPointLabelBold = 0
classicxdmfDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
classicxdmfDisplay.SelectionPointLabelFontFamily = 'Arial'
classicxdmfDisplay.SelectionPointLabelFontFile = ''
classicxdmfDisplay.SelectionPointLabelFontSize = 18
classicxdmfDisplay.SelectionPointLabelItalic = 0
classicxdmfDisplay.SelectionPointLabelJustification = 'Left'
classicxdmfDisplay.SelectionPointLabelOpacity = 1.0
classicxdmfDisplay.SelectionPointLabelShadow = 0
classicxdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
classicxdmfDisplay.ScalarOpacityFunction = None
classicxdmfDisplay.ScalarOpacityUnitDistance = 0.3278395087068577
classicxdmfDisplay.UseSeparateOpacityArray = 0
classicxdmfDisplay.OpacityArrayName = ['POINTS', 'f_105']
classicxdmfDisplay.OpacityComponent = 'X'
classicxdmfDisplay.SelectMapper = 'Projected tetra'
classicxdmfDisplay.SamplingDimensions = [128, 128, 128]
classicxdmfDisplay.UseFloatingPointFrameBuffer = 1
classicxdmfDisplay.SelectInputVectors = ['POINTS', 'f_105']
classicxdmfDisplay.NumberOfSteps = 40
classicxdmfDisplay.StepSize = 0.25
classicxdmfDisplay.NormalizeVectors = 1
classicxdmfDisplay.EnhancedLIC = 1
classicxdmfDisplay.ColorMode = 'Blend'
classicxdmfDisplay.LICIntensity = 0.8
classicxdmfDisplay.MapModeBias = 0.0
classicxdmfDisplay.EnhanceContrast = 'Off'
classicxdmfDisplay.LowLICContrastEnhancementFactor = 0.0
classicxdmfDisplay.HighLICContrastEnhancementFactor = 0.0
classicxdmfDisplay.LowColorContrastEnhancementFactor = 0.0
classicxdmfDisplay.HighColorContrastEnhancementFactor = 0.0
classicxdmfDisplay.AntiAlias = 0
classicxdmfDisplay.MaskOnSurface = 1
classicxdmfDisplay.MaskThreshold = 0.0
classicxdmfDisplay.MaskIntensity = 0.0
classicxdmfDisplay.MaskColor = [0.5, 0.5, 0.5]
classicxdmfDisplay.GenerateNoiseTexture = 0
classicxdmfDisplay.NoiseType = 'Gaussian'
classicxdmfDisplay.NoiseTextureSize = 128
classicxdmfDisplay.NoiseGrainSize = 2
classicxdmfDisplay.MinNoiseValue = 0.0
classicxdmfDisplay.MaxNoiseValue = 0.8
classicxdmfDisplay.NumberOfNoiseLevels = 1024
classicxdmfDisplay.ImpulseNoiseProbability = 1.0
classicxdmfDisplay.ImpulseNoiseBackgroundValue = 0.0
classicxdmfDisplay.NoiseGeneratorSeed = 1
classicxdmfDisplay.CompositeStrategy = 'AUTO'
classicxdmfDisplay.UseLICForLOD = 0
classicxdmfDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
classicxdmfDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
classicxdmfDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
classicxdmfDisplay.GlyphType.TipResolution = 6
classicxdmfDisplay.GlyphType.TipRadius = 0.1
classicxdmfDisplay.GlyphType.TipLength = 0.35
classicxdmfDisplay.GlyphType.ShaftResolution = 6
classicxdmfDisplay.GlyphType.ShaftRadius = 0.03
classicxdmfDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
classicxdmfDisplay.ScaleTransferFunction.Points = [-0.005601954180747271, 0.0, 0.5, 0.0, 0.012777622789144516, 1.0, 0.5, 0.0]
classicxdmfDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
classicxdmfDisplay.OpacityTransferFunction.Points = [-0.005601954180747271, 0.0, 0.5, 0.0, 0.012777622789144516, 1.0, 0.5, 0.0]
classicxdmfDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
classicxdmfDisplay.DataAxesGrid.XTitle = 'X Axis'
classicxdmfDisplay.DataAxesGrid.YTitle = 'Y Axis'
classicxdmfDisplay.DataAxesGrid.ZTitle = 'Z Axis'
classicxdmfDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.XTitleFontFile = ''
classicxdmfDisplay.DataAxesGrid.XTitleBold = 0
classicxdmfDisplay.DataAxesGrid.XTitleItalic = 0
classicxdmfDisplay.DataAxesGrid.XTitleFontSize = 12
classicxdmfDisplay.DataAxesGrid.XTitleShadow = 0
classicxdmfDisplay.DataAxesGrid.XTitleOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.YTitleFontFile = ''
classicxdmfDisplay.DataAxesGrid.YTitleBold = 0
classicxdmfDisplay.DataAxesGrid.YTitleItalic = 0
classicxdmfDisplay.DataAxesGrid.YTitleFontSize = 12
classicxdmfDisplay.DataAxesGrid.YTitleShadow = 0
classicxdmfDisplay.DataAxesGrid.YTitleOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.ZTitleFontFile = ''
classicxdmfDisplay.DataAxesGrid.ZTitleBold = 0
classicxdmfDisplay.DataAxesGrid.ZTitleItalic = 0
classicxdmfDisplay.DataAxesGrid.ZTitleFontSize = 12
classicxdmfDisplay.DataAxesGrid.ZTitleShadow = 0
classicxdmfDisplay.DataAxesGrid.ZTitleOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.FacesToRender = 63
classicxdmfDisplay.DataAxesGrid.CullBackface = 0
classicxdmfDisplay.DataAxesGrid.CullFrontface = 1
classicxdmfDisplay.DataAxesGrid.ShowGrid = 0
classicxdmfDisplay.DataAxesGrid.ShowEdges = 1
classicxdmfDisplay.DataAxesGrid.ShowTicks = 1
classicxdmfDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
classicxdmfDisplay.DataAxesGrid.AxesToLabel = 63
classicxdmfDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.XLabelFontFile = ''
classicxdmfDisplay.DataAxesGrid.XLabelBold = 0
classicxdmfDisplay.DataAxesGrid.XLabelItalic = 0
classicxdmfDisplay.DataAxesGrid.XLabelFontSize = 12
classicxdmfDisplay.DataAxesGrid.XLabelShadow = 0
classicxdmfDisplay.DataAxesGrid.XLabelOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.YLabelFontFile = ''
classicxdmfDisplay.DataAxesGrid.YLabelBold = 0
classicxdmfDisplay.DataAxesGrid.YLabelItalic = 0
classicxdmfDisplay.DataAxesGrid.YLabelFontSize = 12
classicxdmfDisplay.DataAxesGrid.YLabelShadow = 0
classicxdmfDisplay.DataAxesGrid.YLabelOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
classicxdmfDisplay.DataAxesGrid.ZLabelFontFile = ''
classicxdmfDisplay.DataAxesGrid.ZLabelBold = 0
classicxdmfDisplay.DataAxesGrid.ZLabelItalic = 0
classicxdmfDisplay.DataAxesGrid.ZLabelFontSize = 12
classicxdmfDisplay.DataAxesGrid.ZLabelShadow = 0
classicxdmfDisplay.DataAxesGrid.ZLabelOpacity = 1.0
classicxdmfDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
classicxdmfDisplay.DataAxesGrid.XAxisPrecision = 2
classicxdmfDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
classicxdmfDisplay.DataAxesGrid.XAxisLabels = []
classicxdmfDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
classicxdmfDisplay.DataAxesGrid.YAxisPrecision = 2
classicxdmfDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
classicxdmfDisplay.DataAxesGrid.YAxisLabels = []
classicxdmfDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
classicxdmfDisplay.DataAxesGrid.ZAxisPrecision = 2
classicxdmfDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
classicxdmfDisplay.DataAxesGrid.ZAxisLabels = []
classicxdmfDisplay.DataAxesGrid.UseCustomBounds = 0
classicxdmfDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
classicxdmfDisplay.PolarAxes.Visibility = 0
classicxdmfDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
classicxdmfDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
classicxdmfDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
classicxdmfDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
classicxdmfDisplay.PolarAxes.EnableCustomRange = 0
classicxdmfDisplay.PolarAxes.CustomRange = [0.0, 1.0]
classicxdmfDisplay.PolarAxes.PolarAxisVisibility = 1
classicxdmfDisplay.PolarAxes.RadialAxesVisibility = 1
classicxdmfDisplay.PolarAxes.DrawRadialGridlines = 1
classicxdmfDisplay.PolarAxes.PolarArcsVisibility = 1
classicxdmfDisplay.PolarAxes.DrawPolarArcsGridlines = 1
classicxdmfDisplay.PolarAxes.NumberOfRadialAxes = 0
classicxdmfDisplay.PolarAxes.AutoSubdividePolarAxis = 1
classicxdmfDisplay.PolarAxes.NumberOfPolarAxis = 0
classicxdmfDisplay.PolarAxes.MinimumRadius = 0.0
classicxdmfDisplay.PolarAxes.MinimumAngle = 0.0
classicxdmfDisplay.PolarAxes.MaximumAngle = 90.0
classicxdmfDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
classicxdmfDisplay.PolarAxes.Ratio = 1.0
classicxdmfDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
classicxdmfDisplay.PolarAxes.PolarAxisTitleVisibility = 1
classicxdmfDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
classicxdmfDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
classicxdmfDisplay.PolarAxes.PolarLabelVisibility = 1
classicxdmfDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
classicxdmfDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
classicxdmfDisplay.PolarAxes.RadialLabelVisibility = 1
classicxdmfDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
classicxdmfDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
classicxdmfDisplay.PolarAxes.RadialUnitsVisibility = 1
classicxdmfDisplay.PolarAxes.ScreenSize = 10.0
classicxdmfDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
classicxdmfDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
classicxdmfDisplay.PolarAxes.PolarAxisTitleFontFile = ''
classicxdmfDisplay.PolarAxes.PolarAxisTitleBold = 0
classicxdmfDisplay.PolarAxes.PolarAxisTitleItalic = 0
classicxdmfDisplay.PolarAxes.PolarAxisTitleShadow = 0
classicxdmfDisplay.PolarAxes.PolarAxisTitleFontSize = 12
classicxdmfDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
classicxdmfDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
classicxdmfDisplay.PolarAxes.PolarAxisLabelFontFile = ''
classicxdmfDisplay.PolarAxes.PolarAxisLabelBold = 0
classicxdmfDisplay.PolarAxes.PolarAxisLabelItalic = 0
classicxdmfDisplay.PolarAxes.PolarAxisLabelShadow = 0
classicxdmfDisplay.PolarAxes.PolarAxisLabelFontSize = 12
classicxdmfDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
classicxdmfDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
classicxdmfDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
classicxdmfDisplay.PolarAxes.LastRadialAxisTextBold = 0
classicxdmfDisplay.PolarAxes.LastRadialAxisTextItalic = 0
classicxdmfDisplay.PolarAxes.LastRadialAxisTextShadow = 0
classicxdmfDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
classicxdmfDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
classicxdmfDisplay.PolarAxes.EnableDistanceLOD = 1
classicxdmfDisplay.PolarAxes.DistanceLODThreshold = 0.7
classicxdmfDisplay.PolarAxes.EnableViewAngleLOD = 1
classicxdmfDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
classicxdmfDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
classicxdmfDisplay.PolarAxes.PolarTicksVisibility = 1
classicxdmfDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
classicxdmfDisplay.PolarAxes.TickLocation = 'Both'
classicxdmfDisplay.PolarAxes.AxisTickVisibility = 1
classicxdmfDisplay.PolarAxes.AxisMinorTickVisibility = 0
classicxdmfDisplay.PolarAxes.ArcTickVisibility = 1
classicxdmfDisplay.PolarAxes.ArcMinorTickVisibility = 0
classicxdmfDisplay.PolarAxes.DeltaAngleMajor = 10.0
classicxdmfDisplay.PolarAxes.DeltaAngleMinor = 5.0
classicxdmfDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
classicxdmfDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
classicxdmfDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
classicxdmfDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
classicxdmfDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
classicxdmfDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
classicxdmfDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
classicxdmfDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
classicxdmfDisplay.PolarAxes.ArcMajorTickSize = 0.0
classicxdmfDisplay.PolarAxes.ArcTickRatioSize = 0.3
classicxdmfDisplay.PolarAxes.ArcMajorTickThickness = 1.0
classicxdmfDisplay.PolarAxes.ArcTickRatioThickness = 0.5
classicxdmfDisplay.PolarAxes.Use2DMode = 0
classicxdmfDisplay.PolarAxes.UseLogAxis = 0

# get the material library
materialLibrary1 = GetMaterialLibrary()

# reset view to fit data
renderView1.ResetCamera(False)

# hide data in view
Hide(classicxdmf, renderView1)

# show data in view
classicxdmfDisplay = Show(classicxdmf, renderView1, 'UnstructuredGridRepresentation')

# reset view to fit data
renderView1.ResetCamera(False)

# set active source
SetActiveSource(fandisk_cleanpvd)

# show data in view
fandisk_cleanpvdDisplay = Show(fandisk_cleanpvd, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'f_5'
f_5LUT = GetColorTransferFunction('f_5')

# get opacity transfer function/opacity map for 'f_5'
f_5PWF = GetOpacityTransferFunction('f_5')

# trace defaults for the display properties.
fandisk_cleanpvdDisplay.Selection = None
fandisk_cleanpvdDisplay.Representation = 'Surface'
fandisk_cleanpvdDisplay.ColorArrayName = ['POINTS', 'f_5']
fandisk_cleanpvdDisplay.LookupTable = f_5LUT
fandisk_cleanpvdDisplay.MapScalars = 1
fandisk_cleanpvdDisplay.MultiComponentsMapping = 0
fandisk_cleanpvdDisplay.InterpolateScalarsBeforeMapping = 1
fandisk_cleanpvdDisplay.Opacity = 1.0
fandisk_cleanpvdDisplay.PointSize = 2.0
fandisk_cleanpvdDisplay.LineWidth = 1.0
fandisk_cleanpvdDisplay.RenderLinesAsTubes = 0
fandisk_cleanpvdDisplay.RenderPointsAsSpheres = 0
fandisk_cleanpvdDisplay.Interpolation = 'Gouraud'
fandisk_cleanpvdDisplay.Specular = 0.0
fandisk_cleanpvdDisplay.SpecularColor = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.SpecularPower = 100.0
fandisk_cleanpvdDisplay.Luminosity = 0.0
fandisk_cleanpvdDisplay.Ambient = 0.0
fandisk_cleanpvdDisplay.Diffuse = 1.0
fandisk_cleanpvdDisplay.Roughness = 0.3
fandisk_cleanpvdDisplay.Metallic = 0.0
fandisk_cleanpvdDisplay.EdgeTint = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.Anisotropy = 0.0
fandisk_cleanpvdDisplay.AnisotropyRotation = 0.0
fandisk_cleanpvdDisplay.BaseIOR = 1.5
fandisk_cleanpvdDisplay.CoatStrength = 0.0
fandisk_cleanpvdDisplay.CoatIOR = 2.0
fandisk_cleanpvdDisplay.CoatRoughness = 0.0
fandisk_cleanpvdDisplay.CoatColor = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.SelectTCoordArray = 'None'
fandisk_cleanpvdDisplay.SelectNormalArray = 'None'
fandisk_cleanpvdDisplay.SelectTangentArray = 'None'
fandisk_cleanpvdDisplay.Texture = None
fandisk_cleanpvdDisplay.RepeatTextures = 1
fandisk_cleanpvdDisplay.InterpolateTextures = 0
fandisk_cleanpvdDisplay.SeamlessU = 0
fandisk_cleanpvdDisplay.SeamlessV = 0
fandisk_cleanpvdDisplay.UseMipmapTextures = 0
fandisk_cleanpvdDisplay.ShowTexturesOnBackface = 1
fandisk_cleanpvdDisplay.BaseColorTexture = None
fandisk_cleanpvdDisplay.NormalTexture = None
fandisk_cleanpvdDisplay.NormalScale = 1.0
fandisk_cleanpvdDisplay.CoatNormalTexture = None
fandisk_cleanpvdDisplay.CoatNormalScale = 1.0
fandisk_cleanpvdDisplay.MaterialTexture = None
fandisk_cleanpvdDisplay.OcclusionStrength = 1.0
fandisk_cleanpvdDisplay.AnisotropyTexture = None
fandisk_cleanpvdDisplay.EmissiveTexture = None
fandisk_cleanpvdDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.FlipTextures = 0
fandisk_cleanpvdDisplay.BackfaceRepresentation = 'Follow Frontface'
fandisk_cleanpvdDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.BackfaceOpacity = 1.0
fandisk_cleanpvdDisplay.Position = [0.0, 0.0, 0.0]
fandisk_cleanpvdDisplay.Scale = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.Orientation = [0.0, 0.0, 0.0]
fandisk_cleanpvdDisplay.Origin = [0.0, 0.0, 0.0]
fandisk_cleanpvdDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
fandisk_cleanpvdDisplay.Pickable = 1
fandisk_cleanpvdDisplay.Triangulate = 0
fandisk_cleanpvdDisplay.UseShaderReplacements = 0
fandisk_cleanpvdDisplay.ShaderReplacements = ''
fandisk_cleanpvdDisplay.NonlinearSubdivisionLevel = 1
fandisk_cleanpvdDisplay.UseDataPartitions = 0
fandisk_cleanpvdDisplay.OSPRayUseScaleArray = 'All Approximate'
fandisk_cleanpvdDisplay.OSPRayScaleArray = 'f_5'
fandisk_cleanpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
fandisk_cleanpvdDisplay.OSPRayMaterial = 'None'
fandisk_cleanpvdDisplay.BlockSelectors = ['/']
fandisk_cleanpvdDisplay.BlockColors = []
fandisk_cleanpvdDisplay.BlockOpacities = []
fandisk_cleanpvdDisplay.Orient = 0
fandisk_cleanpvdDisplay.OrientationMode = 'Direction'
fandisk_cleanpvdDisplay.SelectOrientationVectors = 'None'
fandisk_cleanpvdDisplay.Scaling = 0
fandisk_cleanpvdDisplay.ScaleMode = 'No Data Scaling Off'
fandisk_cleanpvdDisplay.ScaleFactor = 0.5244500000000002
fandisk_cleanpvdDisplay.SelectScaleArray = 'f_5'
fandisk_cleanpvdDisplay.GlyphType = 'Arrow'
fandisk_cleanpvdDisplay.UseGlyphTable = 0
fandisk_cleanpvdDisplay.GlyphTableIndexArray = 'f_5'
fandisk_cleanpvdDisplay.UseCompositeGlyphTable = 0
fandisk_cleanpvdDisplay.UseGlyphCullingAndLOD = 0
fandisk_cleanpvdDisplay.LODValues = []
fandisk_cleanpvdDisplay.ColorByLODIndex = 0
fandisk_cleanpvdDisplay.GaussianRadius = 0.02622250000000001
fandisk_cleanpvdDisplay.ShaderPreset = 'Sphere'
fandisk_cleanpvdDisplay.CustomTriangleScale = 3
fandisk_cleanpvdDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
fandisk_cleanpvdDisplay.Emissive = 0
fandisk_cleanpvdDisplay.ScaleByArray = 0
fandisk_cleanpvdDisplay.SetScaleArray = ['POINTS', 'f_5']
fandisk_cleanpvdDisplay.ScaleArrayComponent = ''
fandisk_cleanpvdDisplay.UseScaleFunction = 1
fandisk_cleanpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
fandisk_cleanpvdDisplay.OpacityByArray = 0
fandisk_cleanpvdDisplay.OpacityArray = ['POINTS', 'f_5']
fandisk_cleanpvdDisplay.OpacityArrayComponent = ''
fandisk_cleanpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
fandisk_cleanpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
fandisk_cleanpvdDisplay.SelectionCellLabelBold = 0
fandisk_cleanpvdDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
fandisk_cleanpvdDisplay.SelectionCellLabelFontFamily = 'Arial'
fandisk_cleanpvdDisplay.SelectionCellLabelFontFile = ''
fandisk_cleanpvdDisplay.SelectionCellLabelFontSize = 18
fandisk_cleanpvdDisplay.SelectionCellLabelItalic = 0
fandisk_cleanpvdDisplay.SelectionCellLabelJustification = 'Left'
fandisk_cleanpvdDisplay.SelectionCellLabelOpacity = 1.0
fandisk_cleanpvdDisplay.SelectionCellLabelShadow = 0
fandisk_cleanpvdDisplay.SelectionPointLabelBold = 0
fandisk_cleanpvdDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
fandisk_cleanpvdDisplay.SelectionPointLabelFontFamily = 'Arial'
fandisk_cleanpvdDisplay.SelectionPointLabelFontFile = ''
fandisk_cleanpvdDisplay.SelectionPointLabelFontSize = 18
fandisk_cleanpvdDisplay.SelectionPointLabelItalic = 0
fandisk_cleanpvdDisplay.SelectionPointLabelJustification = 'Left'
fandisk_cleanpvdDisplay.SelectionPointLabelOpacity = 1.0
fandisk_cleanpvdDisplay.SelectionPointLabelShadow = 0
fandisk_cleanpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
fandisk_cleanpvdDisplay.ScalarOpacityFunction = f_5PWF
fandisk_cleanpvdDisplay.ScalarOpacityUnitDistance = 0.32433335702394783
fandisk_cleanpvdDisplay.UseSeparateOpacityArray = 0
fandisk_cleanpvdDisplay.OpacityArrayName = ['POINTS', 'f_5']
fandisk_cleanpvdDisplay.OpacityComponent = ''
fandisk_cleanpvdDisplay.SelectMapper = 'Projected tetra'
fandisk_cleanpvdDisplay.SamplingDimensions = [128, 128, 128]
fandisk_cleanpvdDisplay.UseFloatingPointFrameBuffer = 1
fandisk_cleanpvdDisplay.SelectInputVectors = [None, '']
fandisk_cleanpvdDisplay.NumberOfSteps = 40
fandisk_cleanpvdDisplay.StepSize = 0.25
fandisk_cleanpvdDisplay.NormalizeVectors = 1
fandisk_cleanpvdDisplay.EnhancedLIC = 1
fandisk_cleanpvdDisplay.ColorMode = 'Blend'
fandisk_cleanpvdDisplay.LICIntensity = 0.8
fandisk_cleanpvdDisplay.MapModeBias = 0.0
fandisk_cleanpvdDisplay.EnhanceContrast = 'Off'
fandisk_cleanpvdDisplay.LowLICContrastEnhancementFactor = 0.0
fandisk_cleanpvdDisplay.HighLICContrastEnhancementFactor = 0.0
fandisk_cleanpvdDisplay.LowColorContrastEnhancementFactor = 0.0
fandisk_cleanpvdDisplay.HighColorContrastEnhancementFactor = 0.0
fandisk_cleanpvdDisplay.AntiAlias = 0
fandisk_cleanpvdDisplay.MaskOnSurface = 1
fandisk_cleanpvdDisplay.MaskThreshold = 0.0
fandisk_cleanpvdDisplay.MaskIntensity = 0.0
fandisk_cleanpvdDisplay.MaskColor = [0.5, 0.5, 0.5]
fandisk_cleanpvdDisplay.GenerateNoiseTexture = 0
fandisk_cleanpvdDisplay.NoiseType = 'Gaussian'
fandisk_cleanpvdDisplay.NoiseTextureSize = 128
fandisk_cleanpvdDisplay.NoiseGrainSize = 2
fandisk_cleanpvdDisplay.MinNoiseValue = 0.0
fandisk_cleanpvdDisplay.MaxNoiseValue = 0.8
fandisk_cleanpvdDisplay.NumberOfNoiseLevels = 1024
fandisk_cleanpvdDisplay.ImpulseNoiseProbability = 1.0
fandisk_cleanpvdDisplay.ImpulseNoiseBackgroundValue = 0.0
fandisk_cleanpvdDisplay.NoiseGeneratorSeed = 1
fandisk_cleanpvdDisplay.CompositeStrategy = 'AUTO'
fandisk_cleanpvdDisplay.UseLICForLOD = 0
fandisk_cleanpvdDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fandisk_cleanpvdDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fandisk_cleanpvdDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
fandisk_cleanpvdDisplay.GlyphType.TipResolution = 6
fandisk_cleanpvdDisplay.GlyphType.TipRadius = 0.1
fandisk_cleanpvdDisplay.GlyphType.TipLength = 0.35
fandisk_cleanpvdDisplay.GlyphType.ShaftResolution = 6
fandisk_cleanpvdDisplay.GlyphType.ShaftRadius = 0.03
fandisk_cleanpvdDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
fandisk_cleanpvdDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
fandisk_cleanpvdDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
fandisk_cleanpvdDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
fandisk_cleanpvdDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fandisk_cleanpvdDisplay.DataAxesGrid.XTitle = 'X Axis'
fandisk_cleanpvdDisplay.DataAxesGrid.YTitle = 'Y Axis'
fandisk_cleanpvdDisplay.DataAxesGrid.ZTitle = 'Z Axis'
fandisk_cleanpvdDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
fandisk_cleanpvdDisplay.DataAxesGrid.XTitleFontFile = ''
fandisk_cleanpvdDisplay.DataAxesGrid.XTitleBold = 0
fandisk_cleanpvdDisplay.DataAxesGrid.XTitleItalic = 0
fandisk_cleanpvdDisplay.DataAxesGrid.XTitleFontSize = 12
fandisk_cleanpvdDisplay.DataAxesGrid.XTitleShadow = 0
fandisk_cleanpvdDisplay.DataAxesGrid.XTitleOpacity = 1.0
fandisk_cleanpvdDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
fandisk_cleanpvdDisplay.DataAxesGrid.YTitleFontFile = ''
fandisk_cleanpvdDisplay.DataAxesGrid.YTitleBold = 0
fandisk_cleanpvdDisplay.DataAxesGrid.YTitleItalic = 0
fandisk_cleanpvdDisplay.DataAxesGrid.YTitleFontSize = 12
fandisk_cleanpvdDisplay.DataAxesGrid.YTitleShadow = 0
fandisk_cleanpvdDisplay.DataAxesGrid.YTitleOpacity = 1.0
fandisk_cleanpvdDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
fandisk_cleanpvdDisplay.DataAxesGrid.ZTitleFontFile = ''
fandisk_cleanpvdDisplay.DataAxesGrid.ZTitleBold = 0
fandisk_cleanpvdDisplay.DataAxesGrid.ZTitleItalic = 0
fandisk_cleanpvdDisplay.DataAxesGrid.ZTitleFontSize = 12
fandisk_cleanpvdDisplay.DataAxesGrid.ZTitleShadow = 0
fandisk_cleanpvdDisplay.DataAxesGrid.ZTitleOpacity = 1.0
fandisk_cleanpvdDisplay.DataAxesGrid.FacesToRender = 63
fandisk_cleanpvdDisplay.DataAxesGrid.CullBackface = 0
fandisk_cleanpvdDisplay.DataAxesGrid.CullFrontface = 1
fandisk_cleanpvdDisplay.DataAxesGrid.ShowGrid = 0
fandisk_cleanpvdDisplay.DataAxesGrid.ShowEdges = 1
fandisk_cleanpvdDisplay.DataAxesGrid.ShowTicks = 1
fandisk_cleanpvdDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
fandisk_cleanpvdDisplay.DataAxesGrid.AxesToLabel = 63
fandisk_cleanpvdDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
fandisk_cleanpvdDisplay.DataAxesGrid.XLabelFontFile = ''
fandisk_cleanpvdDisplay.DataAxesGrid.XLabelBold = 0
fandisk_cleanpvdDisplay.DataAxesGrid.XLabelItalic = 0
fandisk_cleanpvdDisplay.DataAxesGrid.XLabelFontSize = 12
fandisk_cleanpvdDisplay.DataAxesGrid.XLabelShadow = 0
fandisk_cleanpvdDisplay.DataAxesGrid.XLabelOpacity = 1.0
fandisk_cleanpvdDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
fandisk_cleanpvdDisplay.DataAxesGrid.YLabelFontFile = ''
fandisk_cleanpvdDisplay.DataAxesGrid.YLabelBold = 0
fandisk_cleanpvdDisplay.DataAxesGrid.YLabelItalic = 0
fandisk_cleanpvdDisplay.DataAxesGrid.YLabelFontSize = 12
fandisk_cleanpvdDisplay.DataAxesGrid.YLabelShadow = 0
fandisk_cleanpvdDisplay.DataAxesGrid.YLabelOpacity = 1.0
fandisk_cleanpvdDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
fandisk_cleanpvdDisplay.DataAxesGrid.ZLabelFontFile = ''
fandisk_cleanpvdDisplay.DataAxesGrid.ZLabelBold = 0
fandisk_cleanpvdDisplay.DataAxesGrid.ZLabelItalic = 0
fandisk_cleanpvdDisplay.DataAxesGrid.ZLabelFontSize = 12
fandisk_cleanpvdDisplay.DataAxesGrid.ZLabelShadow = 0
fandisk_cleanpvdDisplay.DataAxesGrid.ZLabelOpacity = 1.0
fandisk_cleanpvdDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
fandisk_cleanpvdDisplay.DataAxesGrid.XAxisPrecision = 2
fandisk_cleanpvdDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
fandisk_cleanpvdDisplay.DataAxesGrid.XAxisLabels = []
fandisk_cleanpvdDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
fandisk_cleanpvdDisplay.DataAxesGrid.YAxisPrecision = 2
fandisk_cleanpvdDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
fandisk_cleanpvdDisplay.DataAxesGrid.YAxisLabels = []
fandisk_cleanpvdDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
fandisk_cleanpvdDisplay.DataAxesGrid.ZAxisPrecision = 2
fandisk_cleanpvdDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
fandisk_cleanpvdDisplay.DataAxesGrid.ZAxisLabels = []
fandisk_cleanpvdDisplay.DataAxesGrid.UseCustomBounds = 0
fandisk_cleanpvdDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fandisk_cleanpvdDisplay.PolarAxes.Visibility = 0
fandisk_cleanpvdDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
fandisk_cleanpvdDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
fandisk_cleanpvdDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
fandisk_cleanpvdDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
fandisk_cleanpvdDisplay.PolarAxes.EnableCustomRange = 0
fandisk_cleanpvdDisplay.PolarAxes.CustomRange = [0.0, 1.0]
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisVisibility = 1
fandisk_cleanpvdDisplay.PolarAxes.RadialAxesVisibility = 1
fandisk_cleanpvdDisplay.PolarAxes.DrawRadialGridlines = 1
fandisk_cleanpvdDisplay.PolarAxes.PolarArcsVisibility = 1
fandisk_cleanpvdDisplay.PolarAxes.DrawPolarArcsGridlines = 1
fandisk_cleanpvdDisplay.PolarAxes.NumberOfRadialAxes = 0
fandisk_cleanpvdDisplay.PolarAxes.AutoSubdividePolarAxis = 1
fandisk_cleanpvdDisplay.PolarAxes.NumberOfPolarAxis = 0
fandisk_cleanpvdDisplay.PolarAxes.MinimumRadius = 0.0
fandisk_cleanpvdDisplay.PolarAxes.MinimumAngle = 0.0
fandisk_cleanpvdDisplay.PolarAxes.MaximumAngle = 90.0
fandisk_cleanpvdDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
fandisk_cleanpvdDisplay.PolarAxes.Ratio = 1.0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTitleVisibility = 1
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
fandisk_cleanpvdDisplay.PolarAxes.PolarLabelVisibility = 1
fandisk_cleanpvdDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
fandisk_cleanpvdDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
fandisk_cleanpvdDisplay.PolarAxes.RadialLabelVisibility = 1
fandisk_cleanpvdDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
fandisk_cleanpvdDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
fandisk_cleanpvdDisplay.PolarAxes.RadialUnitsVisibility = 1
fandisk_cleanpvdDisplay.PolarAxes.ScreenSize = 10.0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTitleBold = 0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTitleItalic = 0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTitleShadow = 0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTitleFontSize = 12
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisLabelBold = 0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisLabelItalic = 0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisLabelShadow = 0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisLabelFontSize = 12
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisTextBold = 0
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisTextItalic = 0
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisTextShadow = 0
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
fandisk_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
fandisk_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
fandisk_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
fandisk_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
fandisk_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
fandisk_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
fandisk_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
fandisk_cleanpvdDisplay.PolarAxes.EnableDistanceLOD = 1
fandisk_cleanpvdDisplay.PolarAxes.DistanceLODThreshold = 0.7
fandisk_cleanpvdDisplay.PolarAxes.EnableViewAngleLOD = 1
fandisk_cleanpvdDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
fandisk_cleanpvdDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
fandisk_cleanpvdDisplay.PolarAxes.PolarTicksVisibility = 1
fandisk_cleanpvdDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
fandisk_cleanpvdDisplay.PolarAxes.TickLocation = 'Both'
fandisk_cleanpvdDisplay.PolarAxes.AxisTickVisibility = 1
fandisk_cleanpvdDisplay.PolarAxes.AxisMinorTickVisibility = 0
fandisk_cleanpvdDisplay.PolarAxes.ArcTickVisibility = 1
fandisk_cleanpvdDisplay.PolarAxes.ArcMinorTickVisibility = 0
fandisk_cleanpvdDisplay.PolarAxes.DeltaAngleMajor = 10.0
fandisk_cleanpvdDisplay.PolarAxes.DeltaAngleMinor = 5.0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
fandisk_cleanpvdDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
fandisk_cleanpvdDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
fandisk_cleanpvdDisplay.PolarAxes.ArcMajorTickSize = 0.0
fandisk_cleanpvdDisplay.PolarAxes.ArcTickRatioSize = 0.3
fandisk_cleanpvdDisplay.PolarAxes.ArcMajorTickThickness = 1.0
fandisk_cleanpvdDisplay.PolarAxes.ArcTickRatioThickness = 0.5
fandisk_cleanpvdDisplay.PolarAxes.Use2DMode = 0
fandisk_cleanpvdDisplay.PolarAxes.UseLogAxis = 0

# show color bar/color legend
fandisk_cleanpvdDisplay.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'f_5'
f_5TF2D = GetTransferFunction2D('f_5')

# set active source
SetActiveSource(fandisk_noisepvd)

# show data in view
fandisk_noisepvdDisplay = Show(fandisk_noisepvd, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
fandisk_noisepvdDisplay.Selection = None
fandisk_noisepvdDisplay.Representation = 'Surface'
fandisk_noisepvdDisplay.ColorArrayName = ['POINTS', 'f_5']
fandisk_noisepvdDisplay.LookupTable = f_5LUT
fandisk_noisepvdDisplay.MapScalars = 1
fandisk_noisepvdDisplay.MultiComponentsMapping = 0
fandisk_noisepvdDisplay.InterpolateScalarsBeforeMapping = 1
fandisk_noisepvdDisplay.Opacity = 1.0
fandisk_noisepvdDisplay.PointSize = 2.0
fandisk_noisepvdDisplay.LineWidth = 1.0
fandisk_noisepvdDisplay.RenderLinesAsTubes = 0
fandisk_noisepvdDisplay.RenderPointsAsSpheres = 0
fandisk_noisepvdDisplay.Interpolation = 'Gouraud'
fandisk_noisepvdDisplay.Specular = 0.0
fandisk_noisepvdDisplay.SpecularColor = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.SpecularPower = 100.0
fandisk_noisepvdDisplay.Luminosity = 0.0
fandisk_noisepvdDisplay.Ambient = 0.0
fandisk_noisepvdDisplay.Diffuse = 1.0
fandisk_noisepvdDisplay.Roughness = 0.3
fandisk_noisepvdDisplay.Metallic = 0.0
fandisk_noisepvdDisplay.EdgeTint = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.Anisotropy = 0.0
fandisk_noisepvdDisplay.AnisotropyRotation = 0.0
fandisk_noisepvdDisplay.BaseIOR = 1.5
fandisk_noisepvdDisplay.CoatStrength = 0.0
fandisk_noisepvdDisplay.CoatIOR = 2.0
fandisk_noisepvdDisplay.CoatRoughness = 0.0
fandisk_noisepvdDisplay.CoatColor = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.SelectTCoordArray = 'None'
fandisk_noisepvdDisplay.SelectNormalArray = 'None'
fandisk_noisepvdDisplay.SelectTangentArray = 'None'
fandisk_noisepvdDisplay.Texture = None
fandisk_noisepvdDisplay.RepeatTextures = 1
fandisk_noisepvdDisplay.InterpolateTextures = 0
fandisk_noisepvdDisplay.SeamlessU = 0
fandisk_noisepvdDisplay.SeamlessV = 0
fandisk_noisepvdDisplay.UseMipmapTextures = 0
fandisk_noisepvdDisplay.ShowTexturesOnBackface = 1
fandisk_noisepvdDisplay.BaseColorTexture = None
fandisk_noisepvdDisplay.NormalTexture = None
fandisk_noisepvdDisplay.NormalScale = 1.0
fandisk_noisepvdDisplay.CoatNormalTexture = None
fandisk_noisepvdDisplay.CoatNormalScale = 1.0
fandisk_noisepvdDisplay.MaterialTexture = None
fandisk_noisepvdDisplay.OcclusionStrength = 1.0
fandisk_noisepvdDisplay.AnisotropyTexture = None
fandisk_noisepvdDisplay.EmissiveTexture = None
fandisk_noisepvdDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.FlipTextures = 0
fandisk_noisepvdDisplay.BackfaceRepresentation = 'Follow Frontface'
fandisk_noisepvdDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.BackfaceOpacity = 1.0
fandisk_noisepvdDisplay.Position = [0.0, 0.0, 0.0]
fandisk_noisepvdDisplay.Scale = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.Orientation = [0.0, 0.0, 0.0]
fandisk_noisepvdDisplay.Origin = [0.0, 0.0, 0.0]
fandisk_noisepvdDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
fandisk_noisepvdDisplay.Pickable = 1
fandisk_noisepvdDisplay.Triangulate = 0
fandisk_noisepvdDisplay.UseShaderReplacements = 0
fandisk_noisepvdDisplay.ShaderReplacements = ''
fandisk_noisepvdDisplay.NonlinearSubdivisionLevel = 1
fandisk_noisepvdDisplay.UseDataPartitions = 0
fandisk_noisepvdDisplay.OSPRayUseScaleArray = 'All Approximate'
fandisk_noisepvdDisplay.OSPRayScaleArray = 'f_5'
fandisk_noisepvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
fandisk_noisepvdDisplay.OSPRayMaterial = 'None'
fandisk_noisepvdDisplay.BlockSelectors = ['/']
fandisk_noisepvdDisplay.BlockColors = []
fandisk_noisepvdDisplay.BlockOpacities = []
fandisk_noisepvdDisplay.Orient = 0
fandisk_noisepvdDisplay.OrientationMode = 'Direction'
fandisk_noisepvdDisplay.SelectOrientationVectors = 'None'
fandisk_noisepvdDisplay.Scaling = 0
fandisk_noisepvdDisplay.ScaleMode = 'No Data Scaling Off'
fandisk_noisepvdDisplay.ScaleFactor = 0.5287606281176987
fandisk_noisepvdDisplay.SelectScaleArray = 'f_5'
fandisk_noisepvdDisplay.GlyphType = 'Arrow'
fandisk_noisepvdDisplay.UseGlyphTable = 0
fandisk_noisepvdDisplay.GlyphTableIndexArray = 'f_5'
fandisk_noisepvdDisplay.UseCompositeGlyphTable = 0
fandisk_noisepvdDisplay.UseGlyphCullingAndLOD = 0
fandisk_noisepvdDisplay.LODValues = []
fandisk_noisepvdDisplay.ColorByLODIndex = 0
fandisk_noisepvdDisplay.GaussianRadius = 0.026438031405884934
fandisk_noisepvdDisplay.ShaderPreset = 'Sphere'
fandisk_noisepvdDisplay.CustomTriangleScale = 3
fandisk_noisepvdDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
fandisk_noisepvdDisplay.Emissive = 0
fandisk_noisepvdDisplay.ScaleByArray = 0
fandisk_noisepvdDisplay.SetScaleArray = ['POINTS', 'f_5']
fandisk_noisepvdDisplay.ScaleArrayComponent = ''
fandisk_noisepvdDisplay.UseScaleFunction = 1
fandisk_noisepvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
fandisk_noisepvdDisplay.OpacityByArray = 0
fandisk_noisepvdDisplay.OpacityArray = ['POINTS', 'f_5']
fandisk_noisepvdDisplay.OpacityArrayComponent = ''
fandisk_noisepvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
fandisk_noisepvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
fandisk_noisepvdDisplay.SelectionCellLabelBold = 0
fandisk_noisepvdDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
fandisk_noisepvdDisplay.SelectionCellLabelFontFamily = 'Arial'
fandisk_noisepvdDisplay.SelectionCellLabelFontFile = ''
fandisk_noisepvdDisplay.SelectionCellLabelFontSize = 18
fandisk_noisepvdDisplay.SelectionCellLabelItalic = 0
fandisk_noisepvdDisplay.SelectionCellLabelJustification = 'Left'
fandisk_noisepvdDisplay.SelectionCellLabelOpacity = 1.0
fandisk_noisepvdDisplay.SelectionCellLabelShadow = 0
fandisk_noisepvdDisplay.SelectionPointLabelBold = 0
fandisk_noisepvdDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
fandisk_noisepvdDisplay.SelectionPointLabelFontFamily = 'Arial'
fandisk_noisepvdDisplay.SelectionPointLabelFontFile = ''
fandisk_noisepvdDisplay.SelectionPointLabelFontSize = 18
fandisk_noisepvdDisplay.SelectionPointLabelItalic = 0
fandisk_noisepvdDisplay.SelectionPointLabelJustification = 'Left'
fandisk_noisepvdDisplay.SelectionPointLabelOpacity = 1.0
fandisk_noisepvdDisplay.SelectionPointLabelShadow = 0
fandisk_noisepvdDisplay.PolarAxes = 'PolarAxesRepresentation'
fandisk_noisepvdDisplay.ScalarOpacityFunction = f_5PWF
fandisk_noisepvdDisplay.ScalarOpacityUnitDistance = 0.33056417754016976
fandisk_noisepvdDisplay.UseSeparateOpacityArray = 0
fandisk_noisepvdDisplay.OpacityArrayName = ['POINTS', 'f_5']
fandisk_noisepvdDisplay.OpacityComponent = ''
fandisk_noisepvdDisplay.SelectMapper = 'Projected tetra'
fandisk_noisepvdDisplay.SamplingDimensions = [128, 128, 128]
fandisk_noisepvdDisplay.UseFloatingPointFrameBuffer = 1
fandisk_noisepvdDisplay.SelectInputVectors = [None, '']
fandisk_noisepvdDisplay.NumberOfSteps = 40
fandisk_noisepvdDisplay.StepSize = 0.25
fandisk_noisepvdDisplay.NormalizeVectors = 1
fandisk_noisepvdDisplay.EnhancedLIC = 1
fandisk_noisepvdDisplay.ColorMode = 'Blend'
fandisk_noisepvdDisplay.LICIntensity = 0.8
fandisk_noisepvdDisplay.MapModeBias = 0.0
fandisk_noisepvdDisplay.EnhanceContrast = 'Off'
fandisk_noisepvdDisplay.LowLICContrastEnhancementFactor = 0.0
fandisk_noisepvdDisplay.HighLICContrastEnhancementFactor = 0.0
fandisk_noisepvdDisplay.LowColorContrastEnhancementFactor = 0.0
fandisk_noisepvdDisplay.HighColorContrastEnhancementFactor = 0.0
fandisk_noisepvdDisplay.AntiAlias = 0
fandisk_noisepvdDisplay.MaskOnSurface = 1
fandisk_noisepvdDisplay.MaskThreshold = 0.0
fandisk_noisepvdDisplay.MaskIntensity = 0.0
fandisk_noisepvdDisplay.MaskColor = [0.5, 0.5, 0.5]
fandisk_noisepvdDisplay.GenerateNoiseTexture = 0
fandisk_noisepvdDisplay.NoiseType = 'Gaussian'
fandisk_noisepvdDisplay.NoiseTextureSize = 128
fandisk_noisepvdDisplay.NoiseGrainSize = 2
fandisk_noisepvdDisplay.MinNoiseValue = 0.0
fandisk_noisepvdDisplay.MaxNoiseValue = 0.8
fandisk_noisepvdDisplay.NumberOfNoiseLevels = 1024
fandisk_noisepvdDisplay.ImpulseNoiseProbability = 1.0
fandisk_noisepvdDisplay.ImpulseNoiseBackgroundValue = 0.0
fandisk_noisepvdDisplay.NoiseGeneratorSeed = 1
fandisk_noisepvdDisplay.CompositeStrategy = 'AUTO'
fandisk_noisepvdDisplay.UseLICForLOD = 0
fandisk_noisepvdDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fandisk_noisepvdDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fandisk_noisepvdDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
fandisk_noisepvdDisplay.GlyphType.TipResolution = 6
fandisk_noisepvdDisplay.GlyphType.TipRadius = 0.1
fandisk_noisepvdDisplay.GlyphType.TipLength = 0.35
fandisk_noisepvdDisplay.GlyphType.ShaftResolution = 6
fandisk_noisepvdDisplay.GlyphType.ShaftRadius = 0.03
fandisk_noisepvdDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
fandisk_noisepvdDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
fandisk_noisepvdDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
fandisk_noisepvdDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
fandisk_noisepvdDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fandisk_noisepvdDisplay.DataAxesGrid.XTitle = 'X Axis'
fandisk_noisepvdDisplay.DataAxesGrid.YTitle = 'Y Axis'
fandisk_noisepvdDisplay.DataAxesGrid.ZTitle = 'Z Axis'
fandisk_noisepvdDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
fandisk_noisepvdDisplay.DataAxesGrid.XTitleFontFile = ''
fandisk_noisepvdDisplay.DataAxesGrid.XTitleBold = 0
fandisk_noisepvdDisplay.DataAxesGrid.XTitleItalic = 0
fandisk_noisepvdDisplay.DataAxesGrid.XTitleFontSize = 12
fandisk_noisepvdDisplay.DataAxesGrid.XTitleShadow = 0
fandisk_noisepvdDisplay.DataAxesGrid.XTitleOpacity = 1.0
fandisk_noisepvdDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
fandisk_noisepvdDisplay.DataAxesGrid.YTitleFontFile = ''
fandisk_noisepvdDisplay.DataAxesGrid.YTitleBold = 0
fandisk_noisepvdDisplay.DataAxesGrid.YTitleItalic = 0
fandisk_noisepvdDisplay.DataAxesGrid.YTitleFontSize = 12
fandisk_noisepvdDisplay.DataAxesGrid.YTitleShadow = 0
fandisk_noisepvdDisplay.DataAxesGrid.YTitleOpacity = 1.0
fandisk_noisepvdDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
fandisk_noisepvdDisplay.DataAxesGrid.ZTitleFontFile = ''
fandisk_noisepvdDisplay.DataAxesGrid.ZTitleBold = 0
fandisk_noisepvdDisplay.DataAxesGrid.ZTitleItalic = 0
fandisk_noisepvdDisplay.DataAxesGrid.ZTitleFontSize = 12
fandisk_noisepvdDisplay.DataAxesGrid.ZTitleShadow = 0
fandisk_noisepvdDisplay.DataAxesGrid.ZTitleOpacity = 1.0
fandisk_noisepvdDisplay.DataAxesGrid.FacesToRender = 63
fandisk_noisepvdDisplay.DataAxesGrid.CullBackface = 0
fandisk_noisepvdDisplay.DataAxesGrid.CullFrontface = 1
fandisk_noisepvdDisplay.DataAxesGrid.ShowGrid = 0
fandisk_noisepvdDisplay.DataAxesGrid.ShowEdges = 1
fandisk_noisepvdDisplay.DataAxesGrid.ShowTicks = 1
fandisk_noisepvdDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
fandisk_noisepvdDisplay.DataAxesGrid.AxesToLabel = 63
fandisk_noisepvdDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
fandisk_noisepvdDisplay.DataAxesGrid.XLabelFontFile = ''
fandisk_noisepvdDisplay.DataAxesGrid.XLabelBold = 0
fandisk_noisepvdDisplay.DataAxesGrid.XLabelItalic = 0
fandisk_noisepvdDisplay.DataAxesGrid.XLabelFontSize = 12
fandisk_noisepvdDisplay.DataAxesGrid.XLabelShadow = 0
fandisk_noisepvdDisplay.DataAxesGrid.XLabelOpacity = 1.0
fandisk_noisepvdDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
fandisk_noisepvdDisplay.DataAxesGrid.YLabelFontFile = ''
fandisk_noisepvdDisplay.DataAxesGrid.YLabelBold = 0
fandisk_noisepvdDisplay.DataAxesGrid.YLabelItalic = 0
fandisk_noisepvdDisplay.DataAxesGrid.YLabelFontSize = 12
fandisk_noisepvdDisplay.DataAxesGrid.YLabelShadow = 0
fandisk_noisepvdDisplay.DataAxesGrid.YLabelOpacity = 1.0
fandisk_noisepvdDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
fandisk_noisepvdDisplay.DataAxesGrid.ZLabelFontFile = ''
fandisk_noisepvdDisplay.DataAxesGrid.ZLabelBold = 0
fandisk_noisepvdDisplay.DataAxesGrid.ZLabelItalic = 0
fandisk_noisepvdDisplay.DataAxesGrid.ZLabelFontSize = 12
fandisk_noisepvdDisplay.DataAxesGrid.ZLabelShadow = 0
fandisk_noisepvdDisplay.DataAxesGrid.ZLabelOpacity = 1.0
fandisk_noisepvdDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
fandisk_noisepvdDisplay.DataAxesGrid.XAxisPrecision = 2
fandisk_noisepvdDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
fandisk_noisepvdDisplay.DataAxesGrid.XAxisLabels = []
fandisk_noisepvdDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
fandisk_noisepvdDisplay.DataAxesGrid.YAxisPrecision = 2
fandisk_noisepvdDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
fandisk_noisepvdDisplay.DataAxesGrid.YAxisLabels = []
fandisk_noisepvdDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
fandisk_noisepvdDisplay.DataAxesGrid.ZAxisPrecision = 2
fandisk_noisepvdDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
fandisk_noisepvdDisplay.DataAxesGrid.ZAxisLabels = []
fandisk_noisepvdDisplay.DataAxesGrid.UseCustomBounds = 0
fandisk_noisepvdDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fandisk_noisepvdDisplay.PolarAxes.Visibility = 0
fandisk_noisepvdDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
fandisk_noisepvdDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
fandisk_noisepvdDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
fandisk_noisepvdDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
fandisk_noisepvdDisplay.PolarAxes.EnableCustomRange = 0
fandisk_noisepvdDisplay.PolarAxes.CustomRange = [0.0, 1.0]
fandisk_noisepvdDisplay.PolarAxes.PolarAxisVisibility = 1
fandisk_noisepvdDisplay.PolarAxes.RadialAxesVisibility = 1
fandisk_noisepvdDisplay.PolarAxes.DrawRadialGridlines = 1
fandisk_noisepvdDisplay.PolarAxes.PolarArcsVisibility = 1
fandisk_noisepvdDisplay.PolarAxes.DrawPolarArcsGridlines = 1
fandisk_noisepvdDisplay.PolarAxes.NumberOfRadialAxes = 0
fandisk_noisepvdDisplay.PolarAxes.AutoSubdividePolarAxis = 1
fandisk_noisepvdDisplay.PolarAxes.NumberOfPolarAxis = 0
fandisk_noisepvdDisplay.PolarAxes.MinimumRadius = 0.0
fandisk_noisepvdDisplay.PolarAxes.MinimumAngle = 0.0
fandisk_noisepvdDisplay.PolarAxes.MaximumAngle = 90.0
fandisk_noisepvdDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
fandisk_noisepvdDisplay.PolarAxes.Ratio = 1.0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTitleVisibility = 1
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
fandisk_noisepvdDisplay.PolarAxes.PolarLabelVisibility = 1
fandisk_noisepvdDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
fandisk_noisepvdDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
fandisk_noisepvdDisplay.PolarAxes.RadialLabelVisibility = 1
fandisk_noisepvdDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
fandisk_noisepvdDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
fandisk_noisepvdDisplay.PolarAxes.RadialUnitsVisibility = 1
fandisk_noisepvdDisplay.PolarAxes.ScreenSize = 10.0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTitleBold = 0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTitleItalic = 0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTitleShadow = 0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTitleFontSize = 12
fandisk_noisepvdDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
fandisk_noisepvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
fandisk_noisepvdDisplay.PolarAxes.PolarAxisLabelBold = 0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisLabelItalic = 0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisLabelShadow = 0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisLabelFontSize = 12
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisTextBold = 0
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisTextItalic = 0
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisTextShadow = 0
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
fandisk_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
fandisk_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
fandisk_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
fandisk_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
fandisk_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
fandisk_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
fandisk_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
fandisk_noisepvdDisplay.PolarAxes.EnableDistanceLOD = 1
fandisk_noisepvdDisplay.PolarAxes.DistanceLODThreshold = 0.7
fandisk_noisepvdDisplay.PolarAxes.EnableViewAngleLOD = 1
fandisk_noisepvdDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
fandisk_noisepvdDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
fandisk_noisepvdDisplay.PolarAxes.PolarTicksVisibility = 1
fandisk_noisepvdDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
fandisk_noisepvdDisplay.PolarAxes.TickLocation = 'Both'
fandisk_noisepvdDisplay.PolarAxes.AxisTickVisibility = 1
fandisk_noisepvdDisplay.PolarAxes.AxisMinorTickVisibility = 0
fandisk_noisepvdDisplay.PolarAxes.ArcTickVisibility = 1
fandisk_noisepvdDisplay.PolarAxes.ArcMinorTickVisibility = 0
fandisk_noisepvdDisplay.PolarAxes.DeltaAngleMajor = 10.0
fandisk_noisepvdDisplay.PolarAxes.DeltaAngleMinor = 5.0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
fandisk_noisepvdDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
fandisk_noisepvdDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
fandisk_noisepvdDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
fandisk_noisepvdDisplay.PolarAxes.ArcMajorTickSize = 0.0
fandisk_noisepvdDisplay.PolarAxes.ArcTickRatioSize = 0.3
fandisk_noisepvdDisplay.PolarAxes.ArcMajorTickThickness = 1.0
fandisk_noisepvdDisplay.PolarAxes.ArcTickRatioThickness = 0.5
fandisk_noisepvdDisplay.PolarAxes.Use2DMode = 0
fandisk_noisepvdDisplay.PolarAxes.UseLogAxis = 0

# show color bar/color legend
fandisk_noisepvdDisplay.SetScalarBarVisibility(renderView1, True)

# turn off scalar coloring
ColorBy(fandisk_noisepvdDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(f_5LUT, renderView1)

# set active source
SetActiveSource(fandisk_noisepvd)

# set active source
SetActiveSource(fandisk_cleanpvd)

# turn off scalar coloring
ColorBy(fandisk_cleanpvdDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(f_5LUT, renderView1)

# set active source
SetActiveSource(classicxdmf)

# hide data in view
Hide(fandisk_noisepvd, renderView1)

# hide data in view
Hide(fandisk_cleanpvd, renderView1)

animationScene1.GoToLast()

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# set active source
SetActiveSource(fandisk_noisepvd)

# show data in view
fandisk_noisepvdDisplay = Show(fandisk_noisepvd, renderView1, 'UnstructuredGridRepresentation')

# hide data in view
Hide(fandisk_noisepvd, renderView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1600, 728)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [13.60406129544837, 4.909309228817746, -6.492559878583715]
renderView1.CameraFocalPoint = [3.019672676720456, -4.00016927053431, -1.038622406683844]
renderView1.CameraViewUp = [-0.4516182456724619, -0.009616592809932323, -0.8921594483714533]
renderView1.CameraParallelScale = 3.8489579118191393

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
