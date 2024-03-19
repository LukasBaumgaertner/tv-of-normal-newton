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
classicxdmf = Xdmf3ReaderS(registrationName='Classic.xdmf', FileName=[os.getcwd() + '/FandiskInpainting/Newton/output/Classic.xdmf'])
classicxdmf.PointArrays = ['f_55']
classicxdmf.CellArrays = []
classicxdmf.Sets = []

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

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
classicxdmfDisplay.OSPRayScaleArray = 'f_55'
classicxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
classicxdmfDisplay.OSPRayMaterial = 'None'
classicxdmfDisplay.BlockSelectors = ['/']
classicxdmfDisplay.BlockColors = []
classicxdmfDisplay.BlockOpacities = []
classicxdmfDisplay.Orient = 0
classicxdmfDisplay.OrientationMode = 'Direction'
classicxdmfDisplay.SelectOrientationVectors = 'f_55'
classicxdmfDisplay.Scaling = 0
classicxdmfDisplay.ScaleMode = 'No Data Scaling Off'
classicxdmfDisplay.ScaleFactor = 0.5244499921798706
classicxdmfDisplay.SelectScaleArray = 'None'
classicxdmfDisplay.GlyphType = 'Arrow'
classicxdmfDisplay.UseGlyphTable = 0
classicxdmfDisplay.GlyphTableIndexArray = 'None'
classicxdmfDisplay.UseCompositeGlyphTable = 0
classicxdmfDisplay.UseGlyphCullingAndLOD = 0
classicxdmfDisplay.LODValues = []
classicxdmfDisplay.ColorByLODIndex = 0
classicxdmfDisplay.GaussianRadius = 0.026222499608993532
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
classicxdmfDisplay.SetScaleArray = ['POINTS', 'f_55']
classicxdmfDisplay.ScaleArrayComponent = 'X'
classicxdmfDisplay.UseScaleFunction = 1
classicxdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
classicxdmfDisplay.OpacityByArray = 0
classicxdmfDisplay.OpacityArray = ['POINTS', 'f_55']
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
classicxdmfDisplay.ScalarOpacityUnitDistance = 0.32276202503224943
classicxdmfDisplay.UseSeparateOpacityArray = 0
classicxdmfDisplay.OpacityArrayName = ['POINTS', 'f_55']
classicxdmfDisplay.OpacityComponent = 'X'
classicxdmfDisplay.SelectMapper = 'Projected tetra'
classicxdmfDisplay.SamplingDimensions = [128, 128, 128]
classicxdmfDisplay.UseFloatingPointFrameBuffer = 1
classicxdmfDisplay.SelectInputVectors = ['POINTS', 'f_55']
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
classicxdmfDisplay.ScaleTransferFunction.Points = [-0.004635875578969717, 0.0, 0.5, 0.0, 0.006065682508051395, 1.0, 0.5, 0.0]
classicxdmfDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
classicxdmfDisplay.OpacityTransferFunction.Points = [-0.004635875578969717, 0.0, 0.5, 0.0, 0.006065682508051395, 1.0, 0.5, 0.0]
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

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'PVD Reader'
initial_fandiskpvd = PVDReader(registrationName='initial_fandisk.pvd', FileName=os.getcwd() + '/FandiskInpainting/initial_fandisk.pvd')
initial_fandiskpvd.CellArrays = []
initial_fandiskpvd.PointArrays = ['f_29']
initial_fandiskpvd.ColumnArrays = []

# show data in view
initial_fandiskpvdDisplay = Show(initial_fandiskpvd, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'f_29'
f_29LUT = GetColorTransferFunction('f_29')

# get opacity transfer function/opacity map for 'f_29'
f_29PWF = GetOpacityTransferFunction('f_29')

# trace defaults for the display properties.
initial_fandiskpvdDisplay.Selection = None
initial_fandiskpvdDisplay.Representation = 'Surface'
initial_fandiskpvdDisplay.ColorArrayName = ['POINTS', 'f_29']
initial_fandiskpvdDisplay.LookupTable = f_29LUT
initial_fandiskpvdDisplay.MapScalars = 1
initial_fandiskpvdDisplay.MultiComponentsMapping = 0
initial_fandiskpvdDisplay.InterpolateScalarsBeforeMapping = 1
initial_fandiskpvdDisplay.Opacity = 1.0
initial_fandiskpvdDisplay.PointSize = 2.0
initial_fandiskpvdDisplay.LineWidth = 1.0
initial_fandiskpvdDisplay.RenderLinesAsTubes = 0
initial_fandiskpvdDisplay.RenderPointsAsSpheres = 0
initial_fandiskpvdDisplay.Interpolation = 'Gouraud'
initial_fandiskpvdDisplay.Specular = 0.0
initial_fandiskpvdDisplay.SpecularColor = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.SpecularPower = 100.0
initial_fandiskpvdDisplay.Luminosity = 0.0
initial_fandiskpvdDisplay.Ambient = 0.0
initial_fandiskpvdDisplay.Diffuse = 1.0
initial_fandiskpvdDisplay.Roughness = 0.3
initial_fandiskpvdDisplay.Metallic = 0.0
initial_fandiskpvdDisplay.EdgeTint = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.Anisotropy = 0.0
initial_fandiskpvdDisplay.AnisotropyRotation = 0.0
initial_fandiskpvdDisplay.BaseIOR = 1.5
initial_fandiskpvdDisplay.CoatStrength = 0.0
initial_fandiskpvdDisplay.CoatIOR = 2.0
initial_fandiskpvdDisplay.CoatRoughness = 0.0
initial_fandiskpvdDisplay.CoatColor = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.SelectTCoordArray = 'None'
initial_fandiskpvdDisplay.SelectNormalArray = 'None'
initial_fandiskpvdDisplay.SelectTangentArray = 'None'
initial_fandiskpvdDisplay.Texture = None
initial_fandiskpvdDisplay.RepeatTextures = 1
initial_fandiskpvdDisplay.InterpolateTextures = 0
initial_fandiskpvdDisplay.SeamlessU = 0
initial_fandiskpvdDisplay.SeamlessV = 0
initial_fandiskpvdDisplay.UseMipmapTextures = 0
initial_fandiskpvdDisplay.ShowTexturesOnBackface = 1
initial_fandiskpvdDisplay.BaseColorTexture = None
initial_fandiskpvdDisplay.NormalTexture = None
initial_fandiskpvdDisplay.NormalScale = 1.0
initial_fandiskpvdDisplay.CoatNormalTexture = None
initial_fandiskpvdDisplay.CoatNormalScale = 1.0
initial_fandiskpvdDisplay.MaterialTexture = None
initial_fandiskpvdDisplay.OcclusionStrength = 1.0
initial_fandiskpvdDisplay.AnisotropyTexture = None
initial_fandiskpvdDisplay.EmissiveTexture = None
initial_fandiskpvdDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.FlipTextures = 0
initial_fandiskpvdDisplay.BackfaceRepresentation = 'Follow Frontface'
initial_fandiskpvdDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.BackfaceOpacity = 1.0
initial_fandiskpvdDisplay.Position = [0.0, 0.0, 0.0]
initial_fandiskpvdDisplay.Scale = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.Orientation = [0.0, 0.0, 0.0]
initial_fandiskpvdDisplay.Origin = [0.0, 0.0, 0.0]
initial_fandiskpvdDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
initial_fandiskpvdDisplay.Pickable = 1
initial_fandiskpvdDisplay.Triangulate = 0
initial_fandiskpvdDisplay.UseShaderReplacements = 0
initial_fandiskpvdDisplay.ShaderReplacements = ''
initial_fandiskpvdDisplay.NonlinearSubdivisionLevel = 1
initial_fandiskpvdDisplay.UseDataPartitions = 0
initial_fandiskpvdDisplay.OSPRayUseScaleArray = 'All Approximate'
initial_fandiskpvdDisplay.OSPRayScaleArray = 'f_29'
initial_fandiskpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
initial_fandiskpvdDisplay.OSPRayMaterial = 'None'
initial_fandiskpvdDisplay.BlockSelectors = ['/']
initial_fandiskpvdDisplay.BlockColors = []
initial_fandiskpvdDisplay.BlockOpacities = []
initial_fandiskpvdDisplay.Orient = 0
initial_fandiskpvdDisplay.OrientationMode = 'Direction'
initial_fandiskpvdDisplay.SelectOrientationVectors = 'None'
initial_fandiskpvdDisplay.Scaling = 0
initial_fandiskpvdDisplay.ScaleMode = 'No Data Scaling Off'
initial_fandiskpvdDisplay.ScaleFactor = 0.5244499921798706
initial_fandiskpvdDisplay.SelectScaleArray = 'f_29'
initial_fandiskpvdDisplay.GlyphType = 'Arrow'
initial_fandiskpvdDisplay.UseGlyphTable = 0
initial_fandiskpvdDisplay.GlyphTableIndexArray = 'f_29'
initial_fandiskpvdDisplay.UseCompositeGlyphTable = 0
initial_fandiskpvdDisplay.UseGlyphCullingAndLOD = 0
initial_fandiskpvdDisplay.LODValues = []
initial_fandiskpvdDisplay.ColorByLODIndex = 0
initial_fandiskpvdDisplay.GaussianRadius = 0.026222499608993532
initial_fandiskpvdDisplay.ShaderPreset = 'Sphere'
initial_fandiskpvdDisplay.CustomTriangleScale = 3
initial_fandiskpvdDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
initial_fandiskpvdDisplay.Emissive = 0
initial_fandiskpvdDisplay.ScaleByArray = 0
initial_fandiskpvdDisplay.SetScaleArray = ['POINTS', 'f_29']
initial_fandiskpvdDisplay.ScaleArrayComponent = ''
initial_fandiskpvdDisplay.UseScaleFunction = 1
initial_fandiskpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
initial_fandiskpvdDisplay.OpacityByArray = 0
initial_fandiskpvdDisplay.OpacityArray = ['POINTS', 'f_29']
initial_fandiskpvdDisplay.OpacityArrayComponent = ''
initial_fandiskpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
initial_fandiskpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
initial_fandiskpvdDisplay.SelectionCellLabelBold = 0
initial_fandiskpvdDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
initial_fandiskpvdDisplay.SelectionCellLabelFontFamily = 'Arial'
initial_fandiskpvdDisplay.SelectionCellLabelFontFile = ''
initial_fandiskpvdDisplay.SelectionCellLabelFontSize = 18
initial_fandiskpvdDisplay.SelectionCellLabelItalic = 0
initial_fandiskpvdDisplay.SelectionCellLabelJustification = 'Left'
initial_fandiskpvdDisplay.SelectionCellLabelOpacity = 1.0
initial_fandiskpvdDisplay.SelectionCellLabelShadow = 0
initial_fandiskpvdDisplay.SelectionPointLabelBold = 0
initial_fandiskpvdDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
initial_fandiskpvdDisplay.SelectionPointLabelFontFamily = 'Arial'
initial_fandiskpvdDisplay.SelectionPointLabelFontFile = ''
initial_fandiskpvdDisplay.SelectionPointLabelFontSize = 18
initial_fandiskpvdDisplay.SelectionPointLabelItalic = 0
initial_fandiskpvdDisplay.SelectionPointLabelJustification = 'Left'
initial_fandiskpvdDisplay.SelectionPointLabelOpacity = 1.0
initial_fandiskpvdDisplay.SelectionPointLabelShadow = 0
initial_fandiskpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
initial_fandiskpvdDisplay.ScalarOpacityFunction = f_29PWF
initial_fandiskpvdDisplay.ScalarOpacityUnitDistance = 0.32276202503224943
initial_fandiskpvdDisplay.UseSeparateOpacityArray = 0
initial_fandiskpvdDisplay.OpacityArrayName = ['POINTS', 'f_29']
initial_fandiskpvdDisplay.OpacityComponent = ''
initial_fandiskpvdDisplay.SelectMapper = 'Projected tetra'
initial_fandiskpvdDisplay.SamplingDimensions = [128, 128, 128]
initial_fandiskpvdDisplay.UseFloatingPointFrameBuffer = 1
initial_fandiskpvdDisplay.SelectInputVectors = [None, '']
initial_fandiskpvdDisplay.NumberOfSteps = 40
initial_fandiskpvdDisplay.StepSize = 0.25
initial_fandiskpvdDisplay.NormalizeVectors = 1
initial_fandiskpvdDisplay.EnhancedLIC = 1
initial_fandiskpvdDisplay.ColorMode = 'Blend'
initial_fandiskpvdDisplay.LICIntensity = 0.8
initial_fandiskpvdDisplay.MapModeBias = 0.0
initial_fandiskpvdDisplay.EnhanceContrast = 'Off'
initial_fandiskpvdDisplay.LowLICContrastEnhancementFactor = 0.0
initial_fandiskpvdDisplay.HighLICContrastEnhancementFactor = 0.0
initial_fandiskpvdDisplay.LowColorContrastEnhancementFactor = 0.0
initial_fandiskpvdDisplay.HighColorContrastEnhancementFactor = 0.0
initial_fandiskpvdDisplay.AntiAlias = 0
initial_fandiskpvdDisplay.MaskOnSurface = 1
initial_fandiskpvdDisplay.MaskThreshold = 0.0
initial_fandiskpvdDisplay.MaskIntensity = 0.0
initial_fandiskpvdDisplay.MaskColor = [0.5, 0.5, 0.5]
initial_fandiskpvdDisplay.GenerateNoiseTexture = 0
initial_fandiskpvdDisplay.NoiseType = 'Gaussian'
initial_fandiskpvdDisplay.NoiseTextureSize = 128
initial_fandiskpvdDisplay.NoiseGrainSize = 2
initial_fandiskpvdDisplay.MinNoiseValue = 0.0
initial_fandiskpvdDisplay.MaxNoiseValue = 0.8
initial_fandiskpvdDisplay.NumberOfNoiseLevels = 1024
initial_fandiskpvdDisplay.ImpulseNoiseProbability = 1.0
initial_fandiskpvdDisplay.ImpulseNoiseBackgroundValue = 0.0
initial_fandiskpvdDisplay.NoiseGeneratorSeed = 1
initial_fandiskpvdDisplay.CompositeStrategy = 'AUTO'
initial_fandiskpvdDisplay.UseLICForLOD = 0
initial_fandiskpvdDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
initial_fandiskpvdDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
initial_fandiskpvdDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
initial_fandiskpvdDisplay.GlyphType.TipResolution = 6
initial_fandiskpvdDisplay.GlyphType.TipRadius = 0.1
initial_fandiskpvdDisplay.GlyphType.TipLength = 0.35
initial_fandiskpvdDisplay.GlyphType.ShaftResolution = 6
initial_fandiskpvdDisplay.GlyphType.ShaftRadius = 0.03
initial_fandiskpvdDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
initial_fandiskpvdDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
initial_fandiskpvdDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
initial_fandiskpvdDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
initial_fandiskpvdDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
initial_fandiskpvdDisplay.DataAxesGrid.XTitle = 'X Axis'
initial_fandiskpvdDisplay.DataAxesGrid.YTitle = 'Y Axis'
initial_fandiskpvdDisplay.DataAxesGrid.ZTitle = 'Z Axis'
initial_fandiskpvdDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
initial_fandiskpvdDisplay.DataAxesGrid.XTitleFontFile = ''
initial_fandiskpvdDisplay.DataAxesGrid.XTitleBold = 0
initial_fandiskpvdDisplay.DataAxesGrid.XTitleItalic = 0
initial_fandiskpvdDisplay.DataAxesGrid.XTitleFontSize = 12
initial_fandiskpvdDisplay.DataAxesGrid.XTitleShadow = 0
initial_fandiskpvdDisplay.DataAxesGrid.XTitleOpacity = 1.0
initial_fandiskpvdDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
initial_fandiskpvdDisplay.DataAxesGrid.YTitleFontFile = ''
initial_fandiskpvdDisplay.DataAxesGrid.YTitleBold = 0
initial_fandiskpvdDisplay.DataAxesGrid.YTitleItalic = 0
initial_fandiskpvdDisplay.DataAxesGrid.YTitleFontSize = 12
initial_fandiskpvdDisplay.DataAxesGrid.YTitleShadow = 0
initial_fandiskpvdDisplay.DataAxesGrid.YTitleOpacity = 1.0
initial_fandiskpvdDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
initial_fandiskpvdDisplay.DataAxesGrid.ZTitleFontFile = ''
initial_fandiskpvdDisplay.DataAxesGrid.ZTitleBold = 0
initial_fandiskpvdDisplay.DataAxesGrid.ZTitleItalic = 0
initial_fandiskpvdDisplay.DataAxesGrid.ZTitleFontSize = 12
initial_fandiskpvdDisplay.DataAxesGrid.ZTitleShadow = 0
initial_fandiskpvdDisplay.DataAxesGrid.ZTitleOpacity = 1.0
initial_fandiskpvdDisplay.DataAxesGrid.FacesToRender = 63
initial_fandiskpvdDisplay.DataAxesGrid.CullBackface = 0
initial_fandiskpvdDisplay.DataAxesGrid.CullFrontface = 1
initial_fandiskpvdDisplay.DataAxesGrid.ShowGrid = 0
initial_fandiskpvdDisplay.DataAxesGrid.ShowEdges = 1
initial_fandiskpvdDisplay.DataAxesGrid.ShowTicks = 1
initial_fandiskpvdDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
initial_fandiskpvdDisplay.DataAxesGrid.AxesToLabel = 63
initial_fandiskpvdDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
initial_fandiskpvdDisplay.DataAxesGrid.XLabelFontFile = ''
initial_fandiskpvdDisplay.DataAxesGrid.XLabelBold = 0
initial_fandiskpvdDisplay.DataAxesGrid.XLabelItalic = 0
initial_fandiskpvdDisplay.DataAxesGrid.XLabelFontSize = 12
initial_fandiskpvdDisplay.DataAxesGrid.XLabelShadow = 0
initial_fandiskpvdDisplay.DataAxesGrid.XLabelOpacity = 1.0
initial_fandiskpvdDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
initial_fandiskpvdDisplay.DataAxesGrid.YLabelFontFile = ''
initial_fandiskpvdDisplay.DataAxesGrid.YLabelBold = 0
initial_fandiskpvdDisplay.DataAxesGrid.YLabelItalic = 0
initial_fandiskpvdDisplay.DataAxesGrid.YLabelFontSize = 12
initial_fandiskpvdDisplay.DataAxesGrid.YLabelShadow = 0
initial_fandiskpvdDisplay.DataAxesGrid.YLabelOpacity = 1.0
initial_fandiskpvdDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
initial_fandiskpvdDisplay.DataAxesGrid.ZLabelFontFile = ''
initial_fandiskpvdDisplay.DataAxesGrid.ZLabelBold = 0
initial_fandiskpvdDisplay.DataAxesGrid.ZLabelItalic = 0
initial_fandiskpvdDisplay.DataAxesGrid.ZLabelFontSize = 12
initial_fandiskpvdDisplay.DataAxesGrid.ZLabelShadow = 0
initial_fandiskpvdDisplay.DataAxesGrid.ZLabelOpacity = 1.0
initial_fandiskpvdDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
initial_fandiskpvdDisplay.DataAxesGrid.XAxisPrecision = 2
initial_fandiskpvdDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
initial_fandiskpvdDisplay.DataAxesGrid.XAxisLabels = []
initial_fandiskpvdDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
initial_fandiskpvdDisplay.DataAxesGrid.YAxisPrecision = 2
initial_fandiskpvdDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
initial_fandiskpvdDisplay.DataAxesGrid.YAxisLabels = []
initial_fandiskpvdDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
initial_fandiskpvdDisplay.DataAxesGrid.ZAxisPrecision = 2
initial_fandiskpvdDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
initial_fandiskpvdDisplay.DataAxesGrid.ZAxisLabels = []
initial_fandiskpvdDisplay.DataAxesGrid.UseCustomBounds = 0
initial_fandiskpvdDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
initial_fandiskpvdDisplay.PolarAxes.Visibility = 0
initial_fandiskpvdDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
initial_fandiskpvdDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
initial_fandiskpvdDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
initial_fandiskpvdDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
initial_fandiskpvdDisplay.PolarAxes.EnableCustomRange = 0
initial_fandiskpvdDisplay.PolarAxes.CustomRange = [0.0, 1.0]
initial_fandiskpvdDisplay.PolarAxes.PolarAxisVisibility = 1
initial_fandiskpvdDisplay.PolarAxes.RadialAxesVisibility = 1
initial_fandiskpvdDisplay.PolarAxes.DrawRadialGridlines = 1
initial_fandiskpvdDisplay.PolarAxes.PolarArcsVisibility = 1
initial_fandiskpvdDisplay.PolarAxes.DrawPolarArcsGridlines = 1
initial_fandiskpvdDisplay.PolarAxes.NumberOfRadialAxes = 0
initial_fandiskpvdDisplay.PolarAxes.AutoSubdividePolarAxis = 1
initial_fandiskpvdDisplay.PolarAxes.NumberOfPolarAxis = 0
initial_fandiskpvdDisplay.PolarAxes.MinimumRadius = 0.0
initial_fandiskpvdDisplay.PolarAxes.MinimumAngle = 0.0
initial_fandiskpvdDisplay.PolarAxes.MaximumAngle = 90.0
initial_fandiskpvdDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
initial_fandiskpvdDisplay.PolarAxes.Ratio = 1.0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTitleVisibility = 1
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
initial_fandiskpvdDisplay.PolarAxes.PolarLabelVisibility = 1
initial_fandiskpvdDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
initial_fandiskpvdDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
initial_fandiskpvdDisplay.PolarAxes.RadialLabelVisibility = 1
initial_fandiskpvdDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
initial_fandiskpvdDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
initial_fandiskpvdDisplay.PolarAxes.RadialUnitsVisibility = 1
initial_fandiskpvdDisplay.PolarAxes.ScreenSize = 10.0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTitleBold = 0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTitleItalic = 0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTitleShadow = 0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTitleFontSize = 12
initial_fandiskpvdDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
initial_fandiskpvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
initial_fandiskpvdDisplay.PolarAxes.PolarAxisLabelBold = 0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisLabelItalic = 0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisLabelShadow = 0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisLabelFontSize = 12
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisTextBold = 0
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisTextItalic = 0
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisTextShadow = 0
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
initial_fandiskpvdDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
initial_fandiskpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
initial_fandiskpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
initial_fandiskpvdDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
initial_fandiskpvdDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
initial_fandiskpvdDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
initial_fandiskpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
initial_fandiskpvdDisplay.PolarAxes.EnableDistanceLOD = 1
initial_fandiskpvdDisplay.PolarAxes.DistanceLODThreshold = 0.7
initial_fandiskpvdDisplay.PolarAxes.EnableViewAngleLOD = 1
initial_fandiskpvdDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
initial_fandiskpvdDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
initial_fandiskpvdDisplay.PolarAxes.PolarTicksVisibility = 1
initial_fandiskpvdDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
initial_fandiskpvdDisplay.PolarAxes.TickLocation = 'Both'
initial_fandiskpvdDisplay.PolarAxes.AxisTickVisibility = 1
initial_fandiskpvdDisplay.PolarAxes.AxisMinorTickVisibility = 0
initial_fandiskpvdDisplay.PolarAxes.ArcTickVisibility = 1
initial_fandiskpvdDisplay.PolarAxes.ArcMinorTickVisibility = 0
initial_fandiskpvdDisplay.PolarAxes.DeltaAngleMajor = 10.0
initial_fandiskpvdDisplay.PolarAxes.DeltaAngleMinor = 5.0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
initial_fandiskpvdDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
initial_fandiskpvdDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
initial_fandiskpvdDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
initial_fandiskpvdDisplay.PolarAxes.ArcMajorTickSize = 0.0
initial_fandiskpvdDisplay.PolarAxes.ArcTickRatioSize = 0.3
initial_fandiskpvdDisplay.PolarAxes.ArcMajorTickThickness = 1.0
initial_fandiskpvdDisplay.PolarAxes.ArcTickRatioThickness = 0.5
initial_fandiskpvdDisplay.PolarAxes.Use2DMode = 0
initial_fandiskpvdDisplay.PolarAxes.UseLogAxis = 0

# show color bar/color legend
initial_fandiskpvdDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'f_29'
f_29TF2D = GetTransferFunction2D('f_29')

# turn off scalar coloring
ColorBy(initial_fandiskpvdDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(f_29LUT, renderView1)

# create a new 'STL Reader'
fandisk_deletedstl = STLReader(registrationName='fandisk_deleted.stl', FileNames=[os.getcwd() + '/FandiskInpainting/fandisk_deleted.stl'])

# show data in view
fandisk_deletedstlDisplay = Show(fandisk_deletedstl, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
fandisk_deletedstlDisplay.Selection = None
fandisk_deletedstlDisplay.Representation = 'Surface'
fandisk_deletedstlDisplay.ColorArrayName = [None, '']
fandisk_deletedstlDisplay.LookupTable = None
fandisk_deletedstlDisplay.MapScalars = 1
fandisk_deletedstlDisplay.MultiComponentsMapping = 0
fandisk_deletedstlDisplay.InterpolateScalarsBeforeMapping = 1
fandisk_deletedstlDisplay.Opacity = 1.0
fandisk_deletedstlDisplay.PointSize = 2.0
fandisk_deletedstlDisplay.LineWidth = 1.0
fandisk_deletedstlDisplay.RenderLinesAsTubes = 0
fandisk_deletedstlDisplay.RenderPointsAsSpheres = 0
fandisk_deletedstlDisplay.Interpolation = 'Gouraud'
fandisk_deletedstlDisplay.Specular = 0.0
fandisk_deletedstlDisplay.SpecularColor = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.SpecularPower = 100.0
fandisk_deletedstlDisplay.Luminosity = 0.0
fandisk_deletedstlDisplay.Ambient = 0.0
fandisk_deletedstlDisplay.Diffuse = 1.0
fandisk_deletedstlDisplay.Roughness = 0.3
fandisk_deletedstlDisplay.Metallic = 0.0
fandisk_deletedstlDisplay.EdgeTint = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.Anisotropy = 0.0
fandisk_deletedstlDisplay.AnisotropyRotation = 0.0
fandisk_deletedstlDisplay.BaseIOR = 1.5
fandisk_deletedstlDisplay.CoatStrength = 0.0
fandisk_deletedstlDisplay.CoatIOR = 2.0
fandisk_deletedstlDisplay.CoatRoughness = 0.0
fandisk_deletedstlDisplay.CoatColor = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.SelectTCoordArray = 'None'
fandisk_deletedstlDisplay.SelectNormalArray = 'None'
fandisk_deletedstlDisplay.SelectTangentArray = 'None'
fandisk_deletedstlDisplay.Texture = None
fandisk_deletedstlDisplay.RepeatTextures = 1
fandisk_deletedstlDisplay.InterpolateTextures = 0
fandisk_deletedstlDisplay.SeamlessU = 0
fandisk_deletedstlDisplay.SeamlessV = 0
fandisk_deletedstlDisplay.UseMipmapTextures = 0
fandisk_deletedstlDisplay.ShowTexturesOnBackface = 1
fandisk_deletedstlDisplay.BaseColorTexture = None
fandisk_deletedstlDisplay.NormalTexture = None
fandisk_deletedstlDisplay.NormalScale = 1.0
fandisk_deletedstlDisplay.CoatNormalTexture = None
fandisk_deletedstlDisplay.CoatNormalScale = 1.0
fandisk_deletedstlDisplay.MaterialTexture = None
fandisk_deletedstlDisplay.OcclusionStrength = 1.0
fandisk_deletedstlDisplay.AnisotropyTexture = None
fandisk_deletedstlDisplay.EmissiveTexture = None
fandisk_deletedstlDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.FlipTextures = 0
fandisk_deletedstlDisplay.BackfaceRepresentation = 'Follow Frontface'
fandisk_deletedstlDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.BackfaceOpacity = 1.0
fandisk_deletedstlDisplay.Position = [0.0, 0.0, 0.0]
fandisk_deletedstlDisplay.Scale = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.Orientation = [0.0, 0.0, 0.0]
fandisk_deletedstlDisplay.Origin = [0.0, 0.0, 0.0]
fandisk_deletedstlDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
fandisk_deletedstlDisplay.Pickable = 1
fandisk_deletedstlDisplay.Triangulate = 0
fandisk_deletedstlDisplay.UseShaderReplacements = 0
fandisk_deletedstlDisplay.ShaderReplacements = ''
fandisk_deletedstlDisplay.NonlinearSubdivisionLevel = 1
fandisk_deletedstlDisplay.UseDataPartitions = 0
fandisk_deletedstlDisplay.OSPRayUseScaleArray = 'All Approximate'
fandisk_deletedstlDisplay.OSPRayScaleArray = ''
fandisk_deletedstlDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
fandisk_deletedstlDisplay.OSPRayMaterial = 'None'
fandisk_deletedstlDisplay.BlockSelectors = ['/']
fandisk_deletedstlDisplay.BlockColors = []
fandisk_deletedstlDisplay.BlockOpacities = []
fandisk_deletedstlDisplay.Orient = 0
fandisk_deletedstlDisplay.OrientationMode = 'Direction'
fandisk_deletedstlDisplay.SelectOrientationVectors = 'None'
fandisk_deletedstlDisplay.Scaling = 0
fandisk_deletedstlDisplay.ScaleMode = 'No Data Scaling Off'
fandisk_deletedstlDisplay.ScaleFactor = 0.5244499921798706
fandisk_deletedstlDisplay.SelectScaleArray = 'None'
fandisk_deletedstlDisplay.GlyphType = 'Arrow'
fandisk_deletedstlDisplay.UseGlyphTable = 0
fandisk_deletedstlDisplay.GlyphTableIndexArray = 'None'
fandisk_deletedstlDisplay.UseCompositeGlyphTable = 0
fandisk_deletedstlDisplay.UseGlyphCullingAndLOD = 0
fandisk_deletedstlDisplay.LODValues = []
fandisk_deletedstlDisplay.ColorByLODIndex = 0
fandisk_deletedstlDisplay.GaussianRadius = 0.026222499608993532
fandisk_deletedstlDisplay.ShaderPreset = 'Sphere'
fandisk_deletedstlDisplay.CustomTriangleScale = 3
fandisk_deletedstlDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
fandisk_deletedstlDisplay.Emissive = 0
fandisk_deletedstlDisplay.ScaleByArray = 0
fandisk_deletedstlDisplay.SetScaleArray = [None, '']
fandisk_deletedstlDisplay.ScaleArrayComponent = 0
fandisk_deletedstlDisplay.UseScaleFunction = 1
fandisk_deletedstlDisplay.ScaleTransferFunction = 'PiecewiseFunction'
fandisk_deletedstlDisplay.OpacityByArray = 0
fandisk_deletedstlDisplay.OpacityArray = [None, '']
fandisk_deletedstlDisplay.OpacityArrayComponent = 0
fandisk_deletedstlDisplay.OpacityTransferFunction = 'PiecewiseFunction'
fandisk_deletedstlDisplay.DataAxesGrid = 'GridAxesRepresentation'
fandisk_deletedstlDisplay.SelectionCellLabelBold = 0
fandisk_deletedstlDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
fandisk_deletedstlDisplay.SelectionCellLabelFontFamily = 'Arial'
fandisk_deletedstlDisplay.SelectionCellLabelFontFile = ''
fandisk_deletedstlDisplay.SelectionCellLabelFontSize = 18
fandisk_deletedstlDisplay.SelectionCellLabelItalic = 0
fandisk_deletedstlDisplay.SelectionCellLabelJustification = 'Left'
fandisk_deletedstlDisplay.SelectionCellLabelOpacity = 1.0
fandisk_deletedstlDisplay.SelectionCellLabelShadow = 0
fandisk_deletedstlDisplay.SelectionPointLabelBold = 0
fandisk_deletedstlDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
fandisk_deletedstlDisplay.SelectionPointLabelFontFamily = 'Arial'
fandisk_deletedstlDisplay.SelectionPointLabelFontFile = ''
fandisk_deletedstlDisplay.SelectionPointLabelFontSize = 18
fandisk_deletedstlDisplay.SelectionPointLabelItalic = 0
fandisk_deletedstlDisplay.SelectionPointLabelJustification = 'Left'
fandisk_deletedstlDisplay.SelectionPointLabelOpacity = 1.0
fandisk_deletedstlDisplay.SelectionPointLabelShadow = 0
fandisk_deletedstlDisplay.PolarAxes = 'PolarAxesRepresentation'
fandisk_deletedstlDisplay.SelectInputVectors = [None, '']
fandisk_deletedstlDisplay.NumberOfSteps = 40
fandisk_deletedstlDisplay.StepSize = 0.25
fandisk_deletedstlDisplay.NormalizeVectors = 1
fandisk_deletedstlDisplay.EnhancedLIC = 1
fandisk_deletedstlDisplay.ColorMode = 'Blend'
fandisk_deletedstlDisplay.LICIntensity = 0.8
fandisk_deletedstlDisplay.MapModeBias = 0.0
fandisk_deletedstlDisplay.EnhanceContrast = 'Off'
fandisk_deletedstlDisplay.LowLICContrastEnhancementFactor = 0.0
fandisk_deletedstlDisplay.HighLICContrastEnhancementFactor = 0.0
fandisk_deletedstlDisplay.LowColorContrastEnhancementFactor = 0.0
fandisk_deletedstlDisplay.HighColorContrastEnhancementFactor = 0.0
fandisk_deletedstlDisplay.AntiAlias = 0
fandisk_deletedstlDisplay.MaskOnSurface = 1
fandisk_deletedstlDisplay.MaskThreshold = 0.0
fandisk_deletedstlDisplay.MaskIntensity = 0.0
fandisk_deletedstlDisplay.MaskColor = [0.5, 0.5, 0.5]
fandisk_deletedstlDisplay.GenerateNoiseTexture = 0
fandisk_deletedstlDisplay.NoiseType = 'Gaussian'
fandisk_deletedstlDisplay.NoiseTextureSize = 128
fandisk_deletedstlDisplay.NoiseGrainSize = 2
fandisk_deletedstlDisplay.MinNoiseValue = 0.0
fandisk_deletedstlDisplay.MaxNoiseValue = 0.8
fandisk_deletedstlDisplay.NumberOfNoiseLevels = 1024
fandisk_deletedstlDisplay.ImpulseNoiseProbability = 1.0
fandisk_deletedstlDisplay.ImpulseNoiseBackgroundValue = 0.0
fandisk_deletedstlDisplay.NoiseGeneratorSeed = 1
fandisk_deletedstlDisplay.CompositeStrategy = 'AUTO'
fandisk_deletedstlDisplay.UseLICForLOD = 0
fandisk_deletedstlDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fandisk_deletedstlDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fandisk_deletedstlDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
fandisk_deletedstlDisplay.GlyphType.TipResolution = 6
fandisk_deletedstlDisplay.GlyphType.TipRadius = 0.1
fandisk_deletedstlDisplay.GlyphType.TipLength = 0.35
fandisk_deletedstlDisplay.GlyphType.ShaftResolution = 6
fandisk_deletedstlDisplay.GlyphType.ShaftRadius = 0.03
fandisk_deletedstlDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
fandisk_deletedstlDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fandisk_deletedstlDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
fandisk_deletedstlDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fandisk_deletedstlDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fandisk_deletedstlDisplay.DataAxesGrid.XTitle = 'X Axis'
fandisk_deletedstlDisplay.DataAxesGrid.YTitle = 'Y Axis'
fandisk_deletedstlDisplay.DataAxesGrid.ZTitle = 'Z Axis'
fandisk_deletedstlDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
fandisk_deletedstlDisplay.DataAxesGrid.XTitleFontFile = ''
fandisk_deletedstlDisplay.DataAxesGrid.XTitleBold = 0
fandisk_deletedstlDisplay.DataAxesGrid.XTitleItalic = 0
fandisk_deletedstlDisplay.DataAxesGrid.XTitleFontSize = 12
fandisk_deletedstlDisplay.DataAxesGrid.XTitleShadow = 0
fandisk_deletedstlDisplay.DataAxesGrid.XTitleOpacity = 1.0
fandisk_deletedstlDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
fandisk_deletedstlDisplay.DataAxesGrid.YTitleFontFile = ''
fandisk_deletedstlDisplay.DataAxesGrid.YTitleBold = 0
fandisk_deletedstlDisplay.DataAxesGrid.YTitleItalic = 0
fandisk_deletedstlDisplay.DataAxesGrid.YTitleFontSize = 12
fandisk_deletedstlDisplay.DataAxesGrid.YTitleShadow = 0
fandisk_deletedstlDisplay.DataAxesGrid.YTitleOpacity = 1.0
fandisk_deletedstlDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
fandisk_deletedstlDisplay.DataAxesGrid.ZTitleFontFile = ''
fandisk_deletedstlDisplay.DataAxesGrid.ZTitleBold = 0
fandisk_deletedstlDisplay.DataAxesGrid.ZTitleItalic = 0
fandisk_deletedstlDisplay.DataAxesGrid.ZTitleFontSize = 12
fandisk_deletedstlDisplay.DataAxesGrid.ZTitleShadow = 0
fandisk_deletedstlDisplay.DataAxesGrid.ZTitleOpacity = 1.0
fandisk_deletedstlDisplay.DataAxesGrid.FacesToRender = 63
fandisk_deletedstlDisplay.DataAxesGrid.CullBackface = 0
fandisk_deletedstlDisplay.DataAxesGrid.CullFrontface = 1
fandisk_deletedstlDisplay.DataAxesGrid.ShowGrid = 0
fandisk_deletedstlDisplay.DataAxesGrid.ShowEdges = 1
fandisk_deletedstlDisplay.DataAxesGrid.ShowTicks = 1
fandisk_deletedstlDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
fandisk_deletedstlDisplay.DataAxesGrid.AxesToLabel = 63
fandisk_deletedstlDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
fandisk_deletedstlDisplay.DataAxesGrid.XLabelFontFile = ''
fandisk_deletedstlDisplay.DataAxesGrid.XLabelBold = 0
fandisk_deletedstlDisplay.DataAxesGrid.XLabelItalic = 0
fandisk_deletedstlDisplay.DataAxesGrid.XLabelFontSize = 12
fandisk_deletedstlDisplay.DataAxesGrid.XLabelShadow = 0
fandisk_deletedstlDisplay.DataAxesGrid.XLabelOpacity = 1.0
fandisk_deletedstlDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
fandisk_deletedstlDisplay.DataAxesGrid.YLabelFontFile = ''
fandisk_deletedstlDisplay.DataAxesGrid.YLabelBold = 0
fandisk_deletedstlDisplay.DataAxesGrid.YLabelItalic = 0
fandisk_deletedstlDisplay.DataAxesGrid.YLabelFontSize = 12
fandisk_deletedstlDisplay.DataAxesGrid.YLabelShadow = 0
fandisk_deletedstlDisplay.DataAxesGrid.YLabelOpacity = 1.0
fandisk_deletedstlDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
fandisk_deletedstlDisplay.DataAxesGrid.ZLabelFontFile = ''
fandisk_deletedstlDisplay.DataAxesGrid.ZLabelBold = 0
fandisk_deletedstlDisplay.DataAxesGrid.ZLabelItalic = 0
fandisk_deletedstlDisplay.DataAxesGrid.ZLabelFontSize = 12
fandisk_deletedstlDisplay.DataAxesGrid.ZLabelShadow = 0
fandisk_deletedstlDisplay.DataAxesGrid.ZLabelOpacity = 1.0
fandisk_deletedstlDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
fandisk_deletedstlDisplay.DataAxesGrid.XAxisPrecision = 2
fandisk_deletedstlDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
fandisk_deletedstlDisplay.DataAxesGrid.XAxisLabels = []
fandisk_deletedstlDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
fandisk_deletedstlDisplay.DataAxesGrid.YAxisPrecision = 2
fandisk_deletedstlDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
fandisk_deletedstlDisplay.DataAxesGrid.YAxisLabels = []
fandisk_deletedstlDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
fandisk_deletedstlDisplay.DataAxesGrid.ZAxisPrecision = 2
fandisk_deletedstlDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
fandisk_deletedstlDisplay.DataAxesGrid.ZAxisLabels = []
fandisk_deletedstlDisplay.DataAxesGrid.UseCustomBounds = 0
fandisk_deletedstlDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fandisk_deletedstlDisplay.PolarAxes.Visibility = 0
fandisk_deletedstlDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
fandisk_deletedstlDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
fandisk_deletedstlDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
fandisk_deletedstlDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
fandisk_deletedstlDisplay.PolarAxes.EnableCustomRange = 0
fandisk_deletedstlDisplay.PolarAxes.CustomRange = [0.0, 1.0]
fandisk_deletedstlDisplay.PolarAxes.PolarAxisVisibility = 1
fandisk_deletedstlDisplay.PolarAxes.RadialAxesVisibility = 1
fandisk_deletedstlDisplay.PolarAxes.DrawRadialGridlines = 1
fandisk_deletedstlDisplay.PolarAxes.PolarArcsVisibility = 1
fandisk_deletedstlDisplay.PolarAxes.DrawPolarArcsGridlines = 1
fandisk_deletedstlDisplay.PolarAxes.NumberOfRadialAxes = 0
fandisk_deletedstlDisplay.PolarAxes.AutoSubdividePolarAxis = 1
fandisk_deletedstlDisplay.PolarAxes.NumberOfPolarAxis = 0
fandisk_deletedstlDisplay.PolarAxes.MinimumRadius = 0.0
fandisk_deletedstlDisplay.PolarAxes.MinimumAngle = 0.0
fandisk_deletedstlDisplay.PolarAxes.MaximumAngle = 90.0
fandisk_deletedstlDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
fandisk_deletedstlDisplay.PolarAxes.Ratio = 1.0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTitleVisibility = 1
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
fandisk_deletedstlDisplay.PolarAxes.PolarLabelVisibility = 1
fandisk_deletedstlDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
fandisk_deletedstlDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
fandisk_deletedstlDisplay.PolarAxes.RadialLabelVisibility = 1
fandisk_deletedstlDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
fandisk_deletedstlDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
fandisk_deletedstlDisplay.PolarAxes.RadialUnitsVisibility = 1
fandisk_deletedstlDisplay.PolarAxes.ScreenSize = 10.0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTitleFontFile = ''
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTitleBold = 0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTitleItalic = 0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTitleShadow = 0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTitleFontSize = 12
fandisk_deletedstlDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
fandisk_deletedstlDisplay.PolarAxes.PolarAxisLabelFontFile = ''
fandisk_deletedstlDisplay.PolarAxes.PolarAxisLabelBold = 0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisLabelItalic = 0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisLabelShadow = 0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisLabelFontSize = 12
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisTextBold = 0
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisTextItalic = 0
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisTextShadow = 0
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
fandisk_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
fandisk_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
fandisk_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
fandisk_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
fandisk_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
fandisk_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
fandisk_deletedstlDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
fandisk_deletedstlDisplay.PolarAxes.EnableDistanceLOD = 1
fandisk_deletedstlDisplay.PolarAxes.DistanceLODThreshold = 0.7
fandisk_deletedstlDisplay.PolarAxes.EnableViewAngleLOD = 1
fandisk_deletedstlDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
fandisk_deletedstlDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
fandisk_deletedstlDisplay.PolarAxes.PolarTicksVisibility = 1
fandisk_deletedstlDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
fandisk_deletedstlDisplay.PolarAxes.TickLocation = 'Both'
fandisk_deletedstlDisplay.PolarAxes.AxisTickVisibility = 1
fandisk_deletedstlDisplay.PolarAxes.AxisMinorTickVisibility = 0
fandisk_deletedstlDisplay.PolarAxes.ArcTickVisibility = 1
fandisk_deletedstlDisplay.PolarAxes.ArcMinorTickVisibility = 0
fandisk_deletedstlDisplay.PolarAxes.DeltaAngleMajor = 10.0
fandisk_deletedstlDisplay.PolarAxes.DeltaAngleMinor = 5.0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
fandisk_deletedstlDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
fandisk_deletedstlDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
fandisk_deletedstlDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
fandisk_deletedstlDisplay.PolarAxes.ArcMajorTickSize = 0.0
fandisk_deletedstlDisplay.PolarAxes.ArcTickRatioSize = 0.3
fandisk_deletedstlDisplay.PolarAxes.ArcMajorTickThickness = 1.0
fandisk_deletedstlDisplay.PolarAxes.ArcTickRatioThickness = 0.5
fandisk_deletedstlDisplay.PolarAxes.Use2DMode = 0
fandisk_deletedstlDisplay.PolarAxes.UseLogAxis = 0

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(classicxdmf)

animationScene1.GoToLast()

# hide data in view
Hide(initial_fandiskpvd, renderView1)

# hide data in view
Hide(fandisk_deletedstl, renderView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(960, 400)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [11.928082639024094, 5.259267825850913, -7.0019676718297275]
renderView1.CameraFocalPoint = [-0.1860499382019043, 0.22774994373321533, -0.3401299715042114]
renderView1.CameraViewUp = [-0.44770142676126234, -0.09876541325898602, -0.8887118912334367]
renderView1.CameraParallelScale = 3.8077943272176795

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
