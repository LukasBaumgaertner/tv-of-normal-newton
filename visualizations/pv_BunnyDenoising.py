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
classicxdmf = Xdmf3ReaderS(registrationName='Classic.xdmf', FileName=[os.getcwd() + '/Bunny/Newton/output/Classic.xdmf'])
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
bunny_cleanpvd = PVDReader(registrationName='bunny_clean.pvd', FileName=os.getcwd() + '/Bunny/bunny_clean.pvd')
bunny_cleanpvd.CellArrays = ['f_5']
bunny_cleanpvd.PointArrays = []
bunny_cleanpvd.ColumnArrays = []

# create a new 'PVD Reader'
bunny_noisepvd = PVDReader(registrationName='bunny_noise.pvd', FileName=os.getcwd() + '/Bunny/bunny_noise.pvd')
bunny_noisepvd.CellArrays = ['f_5']
bunny_noisepvd.PointArrays = []
bunny_noisepvd.ColumnArrays = []

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
classicxdmfDisplay.ScaleFactor = 0.31233100891113286
classicxdmfDisplay.SelectScaleArray = 'None'
classicxdmfDisplay.GlyphType = 'Arrow'
classicxdmfDisplay.UseGlyphTable = 0
classicxdmfDisplay.GlyphTableIndexArray = 'None'
classicxdmfDisplay.UseCompositeGlyphTable = 0
classicxdmfDisplay.UseGlyphCullingAndLOD = 0
classicxdmfDisplay.LODValues = []
classicxdmfDisplay.ColorByLODIndex = 0
classicxdmfDisplay.GaussianRadius = 0.015616550445556642
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
classicxdmfDisplay.ScalarOpacityUnitDistance = 0.1221484995207334
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
classicxdmfDisplay.ScaleTransferFunction.Points = [-0.002106575993821025, 0.0, 0.5, 0.0, 0.0023171284701675177, 1.0, 0.5, 0.0]
classicxdmfDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
classicxdmfDisplay.OpacityTransferFunction.Points = [-0.002106575993821025, 0.0, 0.5, 0.0, 0.0023171284701675177, 1.0, 0.5, 0.0]
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

# set active source
SetActiveSource(bunny_cleanpvd)

# show data in view
bunny_cleanpvdDisplay = Show(bunny_cleanpvd, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'f_5'
f_5LUT = GetColorTransferFunction('f_5')

# get opacity transfer function/opacity map for 'f_5'
f_5PWF = GetOpacityTransferFunction('f_5')

# trace defaults for the display properties.
bunny_cleanpvdDisplay.Selection = None
bunny_cleanpvdDisplay.Representation = 'Surface'
bunny_cleanpvdDisplay.ColorArrayName = ['CELLS', 'f_5']
bunny_cleanpvdDisplay.LookupTable = f_5LUT
bunny_cleanpvdDisplay.MapScalars = 1
bunny_cleanpvdDisplay.MultiComponentsMapping = 0
bunny_cleanpvdDisplay.InterpolateScalarsBeforeMapping = 1
bunny_cleanpvdDisplay.Opacity = 1.0
bunny_cleanpvdDisplay.PointSize = 2.0
bunny_cleanpvdDisplay.LineWidth = 1.0
bunny_cleanpvdDisplay.RenderLinesAsTubes = 0
bunny_cleanpvdDisplay.RenderPointsAsSpheres = 0
bunny_cleanpvdDisplay.Interpolation = 'Gouraud'
bunny_cleanpvdDisplay.Specular = 0.0
bunny_cleanpvdDisplay.SpecularColor = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.SpecularPower = 100.0
bunny_cleanpvdDisplay.Luminosity = 0.0
bunny_cleanpvdDisplay.Ambient = 0.0
bunny_cleanpvdDisplay.Diffuse = 1.0
bunny_cleanpvdDisplay.Roughness = 0.3
bunny_cleanpvdDisplay.Metallic = 0.0
bunny_cleanpvdDisplay.EdgeTint = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.Anisotropy = 0.0
bunny_cleanpvdDisplay.AnisotropyRotation = 0.0
bunny_cleanpvdDisplay.BaseIOR = 1.5
bunny_cleanpvdDisplay.CoatStrength = 0.0
bunny_cleanpvdDisplay.CoatIOR = 2.0
bunny_cleanpvdDisplay.CoatRoughness = 0.0
bunny_cleanpvdDisplay.CoatColor = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.SelectTCoordArray = 'None'
bunny_cleanpvdDisplay.SelectNormalArray = 'None'
bunny_cleanpvdDisplay.SelectTangentArray = 'None'
bunny_cleanpvdDisplay.Texture = None
bunny_cleanpvdDisplay.RepeatTextures = 1
bunny_cleanpvdDisplay.InterpolateTextures = 0
bunny_cleanpvdDisplay.SeamlessU = 0
bunny_cleanpvdDisplay.SeamlessV = 0
bunny_cleanpvdDisplay.UseMipmapTextures = 0
bunny_cleanpvdDisplay.ShowTexturesOnBackface = 1
bunny_cleanpvdDisplay.BaseColorTexture = None
bunny_cleanpvdDisplay.NormalTexture = None
bunny_cleanpvdDisplay.NormalScale = 1.0
bunny_cleanpvdDisplay.CoatNormalTexture = None
bunny_cleanpvdDisplay.CoatNormalScale = 1.0
bunny_cleanpvdDisplay.MaterialTexture = None
bunny_cleanpvdDisplay.OcclusionStrength = 1.0
bunny_cleanpvdDisplay.AnisotropyTexture = None
bunny_cleanpvdDisplay.EmissiveTexture = None
bunny_cleanpvdDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.FlipTextures = 0
bunny_cleanpvdDisplay.BackfaceRepresentation = 'Follow Frontface'
bunny_cleanpvdDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.BackfaceOpacity = 1.0
bunny_cleanpvdDisplay.Position = [0.0, 0.0, 0.0]
bunny_cleanpvdDisplay.Scale = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.Orientation = [0.0, 0.0, 0.0]
bunny_cleanpvdDisplay.Origin = [0.0, 0.0, 0.0]
bunny_cleanpvdDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
bunny_cleanpvdDisplay.Pickable = 1
bunny_cleanpvdDisplay.Triangulate = 0
bunny_cleanpvdDisplay.UseShaderReplacements = 0
bunny_cleanpvdDisplay.ShaderReplacements = ''
bunny_cleanpvdDisplay.NonlinearSubdivisionLevel = 1
bunny_cleanpvdDisplay.UseDataPartitions = 0
bunny_cleanpvdDisplay.OSPRayUseScaleArray = 'All Approximate'
bunny_cleanpvdDisplay.OSPRayScaleArray = ''
bunny_cleanpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
bunny_cleanpvdDisplay.OSPRayMaterial = 'None'
bunny_cleanpvdDisplay.BlockSelectors = ['/']
bunny_cleanpvdDisplay.BlockColors = []
bunny_cleanpvdDisplay.BlockOpacities = []
bunny_cleanpvdDisplay.Orient = 0
bunny_cleanpvdDisplay.OrientationMode = 'Direction'
bunny_cleanpvdDisplay.SelectOrientationVectors = 'None'
bunny_cleanpvdDisplay.Scaling = 0
bunny_cleanpvdDisplay.ScaleMode = 'No Data Scaling Off'
bunny_cleanpvdDisplay.ScaleFactor = 0.31139800000000006
bunny_cleanpvdDisplay.SelectScaleArray = 'f_5'
bunny_cleanpvdDisplay.GlyphType = 'Arrow'
bunny_cleanpvdDisplay.UseGlyphTable = 0
bunny_cleanpvdDisplay.GlyphTableIndexArray = 'f_5'
bunny_cleanpvdDisplay.UseCompositeGlyphTable = 0
bunny_cleanpvdDisplay.UseGlyphCullingAndLOD = 0
bunny_cleanpvdDisplay.LODValues = []
bunny_cleanpvdDisplay.ColorByLODIndex = 0
bunny_cleanpvdDisplay.GaussianRadius = 0.015569900000000001
bunny_cleanpvdDisplay.ShaderPreset = 'Sphere'
bunny_cleanpvdDisplay.CustomTriangleScale = 3
bunny_cleanpvdDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
bunny_cleanpvdDisplay.Emissive = 0
bunny_cleanpvdDisplay.ScaleByArray = 0
bunny_cleanpvdDisplay.SetScaleArray = [None, '']
bunny_cleanpvdDisplay.ScaleArrayComponent = 0
bunny_cleanpvdDisplay.UseScaleFunction = 1
bunny_cleanpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
bunny_cleanpvdDisplay.OpacityByArray = 0
bunny_cleanpvdDisplay.OpacityArray = [None, '']
bunny_cleanpvdDisplay.OpacityArrayComponent = 0
bunny_cleanpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
bunny_cleanpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
bunny_cleanpvdDisplay.SelectionCellLabelBold = 0
bunny_cleanpvdDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
bunny_cleanpvdDisplay.SelectionCellLabelFontFamily = 'Arial'
bunny_cleanpvdDisplay.SelectionCellLabelFontFile = ''
bunny_cleanpvdDisplay.SelectionCellLabelFontSize = 18
bunny_cleanpvdDisplay.SelectionCellLabelItalic = 0
bunny_cleanpvdDisplay.SelectionCellLabelJustification = 'Left'
bunny_cleanpvdDisplay.SelectionCellLabelOpacity = 1.0
bunny_cleanpvdDisplay.SelectionCellLabelShadow = 0
bunny_cleanpvdDisplay.SelectionPointLabelBold = 0
bunny_cleanpvdDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
bunny_cleanpvdDisplay.SelectionPointLabelFontFamily = 'Arial'
bunny_cleanpvdDisplay.SelectionPointLabelFontFile = ''
bunny_cleanpvdDisplay.SelectionPointLabelFontSize = 18
bunny_cleanpvdDisplay.SelectionPointLabelItalic = 0
bunny_cleanpvdDisplay.SelectionPointLabelJustification = 'Left'
bunny_cleanpvdDisplay.SelectionPointLabelOpacity = 1.0
bunny_cleanpvdDisplay.SelectionPointLabelShadow = 0
bunny_cleanpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
bunny_cleanpvdDisplay.ScalarOpacityFunction = f_5PWF
bunny_cleanpvdDisplay.ScalarOpacityUnitDistance = 0.12165550236396092
bunny_cleanpvdDisplay.UseSeparateOpacityArray = 0
bunny_cleanpvdDisplay.OpacityArrayName = ['CELLS', 'f_5']
bunny_cleanpvdDisplay.OpacityComponent = ''
bunny_cleanpvdDisplay.SelectMapper = 'Projected tetra'
bunny_cleanpvdDisplay.SamplingDimensions = [128, 128, 128]
bunny_cleanpvdDisplay.UseFloatingPointFrameBuffer = 1
bunny_cleanpvdDisplay.SelectInputVectors = [None, '']
bunny_cleanpvdDisplay.NumberOfSteps = 40
bunny_cleanpvdDisplay.StepSize = 0.25
bunny_cleanpvdDisplay.NormalizeVectors = 1
bunny_cleanpvdDisplay.EnhancedLIC = 1
bunny_cleanpvdDisplay.ColorMode = 'Blend'
bunny_cleanpvdDisplay.LICIntensity = 0.8
bunny_cleanpvdDisplay.MapModeBias = 0.0
bunny_cleanpvdDisplay.EnhanceContrast = 'Off'
bunny_cleanpvdDisplay.LowLICContrastEnhancementFactor = 0.0
bunny_cleanpvdDisplay.HighLICContrastEnhancementFactor = 0.0
bunny_cleanpvdDisplay.LowColorContrastEnhancementFactor = 0.0
bunny_cleanpvdDisplay.HighColorContrastEnhancementFactor = 0.0
bunny_cleanpvdDisplay.AntiAlias = 0
bunny_cleanpvdDisplay.MaskOnSurface = 1
bunny_cleanpvdDisplay.MaskThreshold = 0.0
bunny_cleanpvdDisplay.MaskIntensity = 0.0
bunny_cleanpvdDisplay.MaskColor = [0.5, 0.5, 0.5]
bunny_cleanpvdDisplay.GenerateNoiseTexture = 0
bunny_cleanpvdDisplay.NoiseType = 'Gaussian'
bunny_cleanpvdDisplay.NoiseTextureSize = 128
bunny_cleanpvdDisplay.NoiseGrainSize = 2
bunny_cleanpvdDisplay.MinNoiseValue = 0.0
bunny_cleanpvdDisplay.MaxNoiseValue = 0.8
bunny_cleanpvdDisplay.NumberOfNoiseLevels = 1024
bunny_cleanpvdDisplay.ImpulseNoiseProbability = 1.0
bunny_cleanpvdDisplay.ImpulseNoiseBackgroundValue = 0.0
bunny_cleanpvdDisplay.NoiseGeneratorSeed = 1
bunny_cleanpvdDisplay.CompositeStrategy = 'AUTO'
bunny_cleanpvdDisplay.UseLICForLOD = 0
bunny_cleanpvdDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
bunny_cleanpvdDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
bunny_cleanpvdDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
bunny_cleanpvdDisplay.GlyphType.TipResolution = 6
bunny_cleanpvdDisplay.GlyphType.TipRadius = 0.1
bunny_cleanpvdDisplay.GlyphType.TipLength = 0.35
bunny_cleanpvdDisplay.GlyphType.ShaftResolution = 6
bunny_cleanpvdDisplay.GlyphType.ShaftRadius = 0.03
bunny_cleanpvdDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
bunny_cleanpvdDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
bunny_cleanpvdDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
bunny_cleanpvdDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
bunny_cleanpvdDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
bunny_cleanpvdDisplay.DataAxesGrid.XTitle = 'X Axis'
bunny_cleanpvdDisplay.DataAxesGrid.YTitle = 'Y Axis'
bunny_cleanpvdDisplay.DataAxesGrid.ZTitle = 'Z Axis'
bunny_cleanpvdDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
bunny_cleanpvdDisplay.DataAxesGrid.XTitleFontFile = ''
bunny_cleanpvdDisplay.DataAxesGrid.XTitleBold = 0
bunny_cleanpvdDisplay.DataAxesGrid.XTitleItalic = 0
bunny_cleanpvdDisplay.DataAxesGrid.XTitleFontSize = 12
bunny_cleanpvdDisplay.DataAxesGrid.XTitleShadow = 0
bunny_cleanpvdDisplay.DataAxesGrid.XTitleOpacity = 1.0
bunny_cleanpvdDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
bunny_cleanpvdDisplay.DataAxesGrid.YTitleFontFile = ''
bunny_cleanpvdDisplay.DataAxesGrid.YTitleBold = 0
bunny_cleanpvdDisplay.DataAxesGrid.YTitleItalic = 0
bunny_cleanpvdDisplay.DataAxesGrid.YTitleFontSize = 12
bunny_cleanpvdDisplay.DataAxesGrid.YTitleShadow = 0
bunny_cleanpvdDisplay.DataAxesGrid.YTitleOpacity = 1.0
bunny_cleanpvdDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
bunny_cleanpvdDisplay.DataAxesGrid.ZTitleFontFile = ''
bunny_cleanpvdDisplay.DataAxesGrid.ZTitleBold = 0
bunny_cleanpvdDisplay.DataAxesGrid.ZTitleItalic = 0
bunny_cleanpvdDisplay.DataAxesGrid.ZTitleFontSize = 12
bunny_cleanpvdDisplay.DataAxesGrid.ZTitleShadow = 0
bunny_cleanpvdDisplay.DataAxesGrid.ZTitleOpacity = 1.0
bunny_cleanpvdDisplay.DataAxesGrid.FacesToRender = 63
bunny_cleanpvdDisplay.DataAxesGrid.CullBackface = 0
bunny_cleanpvdDisplay.DataAxesGrid.CullFrontface = 1
bunny_cleanpvdDisplay.DataAxesGrid.ShowGrid = 0
bunny_cleanpvdDisplay.DataAxesGrid.ShowEdges = 1
bunny_cleanpvdDisplay.DataAxesGrid.ShowTicks = 1
bunny_cleanpvdDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
bunny_cleanpvdDisplay.DataAxesGrid.AxesToLabel = 63
bunny_cleanpvdDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
bunny_cleanpvdDisplay.DataAxesGrid.XLabelFontFile = ''
bunny_cleanpvdDisplay.DataAxesGrid.XLabelBold = 0
bunny_cleanpvdDisplay.DataAxesGrid.XLabelItalic = 0
bunny_cleanpvdDisplay.DataAxesGrid.XLabelFontSize = 12
bunny_cleanpvdDisplay.DataAxesGrid.XLabelShadow = 0
bunny_cleanpvdDisplay.DataAxesGrid.XLabelOpacity = 1.0
bunny_cleanpvdDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
bunny_cleanpvdDisplay.DataAxesGrid.YLabelFontFile = ''
bunny_cleanpvdDisplay.DataAxesGrid.YLabelBold = 0
bunny_cleanpvdDisplay.DataAxesGrid.YLabelItalic = 0
bunny_cleanpvdDisplay.DataAxesGrid.YLabelFontSize = 12
bunny_cleanpvdDisplay.DataAxesGrid.YLabelShadow = 0
bunny_cleanpvdDisplay.DataAxesGrid.YLabelOpacity = 1.0
bunny_cleanpvdDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
bunny_cleanpvdDisplay.DataAxesGrid.ZLabelFontFile = ''
bunny_cleanpvdDisplay.DataAxesGrid.ZLabelBold = 0
bunny_cleanpvdDisplay.DataAxesGrid.ZLabelItalic = 0
bunny_cleanpvdDisplay.DataAxesGrid.ZLabelFontSize = 12
bunny_cleanpvdDisplay.DataAxesGrid.ZLabelShadow = 0
bunny_cleanpvdDisplay.DataAxesGrid.ZLabelOpacity = 1.0
bunny_cleanpvdDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
bunny_cleanpvdDisplay.DataAxesGrid.XAxisPrecision = 2
bunny_cleanpvdDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
bunny_cleanpvdDisplay.DataAxesGrid.XAxisLabels = []
bunny_cleanpvdDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
bunny_cleanpvdDisplay.DataAxesGrid.YAxisPrecision = 2
bunny_cleanpvdDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
bunny_cleanpvdDisplay.DataAxesGrid.YAxisLabels = []
bunny_cleanpvdDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
bunny_cleanpvdDisplay.DataAxesGrid.ZAxisPrecision = 2
bunny_cleanpvdDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
bunny_cleanpvdDisplay.DataAxesGrid.ZAxisLabels = []
bunny_cleanpvdDisplay.DataAxesGrid.UseCustomBounds = 0
bunny_cleanpvdDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
bunny_cleanpvdDisplay.PolarAxes.Visibility = 0
bunny_cleanpvdDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
bunny_cleanpvdDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
bunny_cleanpvdDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
bunny_cleanpvdDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
bunny_cleanpvdDisplay.PolarAxes.EnableCustomRange = 0
bunny_cleanpvdDisplay.PolarAxes.CustomRange = [0.0, 1.0]
bunny_cleanpvdDisplay.PolarAxes.PolarAxisVisibility = 1
bunny_cleanpvdDisplay.PolarAxes.RadialAxesVisibility = 1
bunny_cleanpvdDisplay.PolarAxes.DrawRadialGridlines = 1
bunny_cleanpvdDisplay.PolarAxes.PolarArcsVisibility = 1
bunny_cleanpvdDisplay.PolarAxes.DrawPolarArcsGridlines = 1
bunny_cleanpvdDisplay.PolarAxes.NumberOfRadialAxes = 0
bunny_cleanpvdDisplay.PolarAxes.AutoSubdividePolarAxis = 1
bunny_cleanpvdDisplay.PolarAxes.NumberOfPolarAxis = 0
bunny_cleanpvdDisplay.PolarAxes.MinimumRadius = 0.0
bunny_cleanpvdDisplay.PolarAxes.MinimumAngle = 0.0
bunny_cleanpvdDisplay.PolarAxes.MaximumAngle = 90.0
bunny_cleanpvdDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
bunny_cleanpvdDisplay.PolarAxes.Ratio = 1.0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTitleVisibility = 1
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
bunny_cleanpvdDisplay.PolarAxes.PolarLabelVisibility = 1
bunny_cleanpvdDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
bunny_cleanpvdDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
bunny_cleanpvdDisplay.PolarAxes.RadialLabelVisibility = 1
bunny_cleanpvdDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
bunny_cleanpvdDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
bunny_cleanpvdDisplay.PolarAxes.RadialUnitsVisibility = 1
bunny_cleanpvdDisplay.PolarAxes.ScreenSize = 10.0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTitleBold = 0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTitleItalic = 0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTitleShadow = 0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTitleFontSize = 12
bunny_cleanpvdDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
bunny_cleanpvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
bunny_cleanpvdDisplay.PolarAxes.PolarAxisLabelBold = 0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisLabelItalic = 0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisLabelShadow = 0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisLabelFontSize = 12
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisTextBold = 0
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisTextItalic = 0
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisTextShadow = 0
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
bunny_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
bunny_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
bunny_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
bunny_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
bunny_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
bunny_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
bunny_cleanpvdDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
bunny_cleanpvdDisplay.PolarAxes.EnableDistanceLOD = 1
bunny_cleanpvdDisplay.PolarAxes.DistanceLODThreshold = 0.7
bunny_cleanpvdDisplay.PolarAxes.EnableViewAngleLOD = 1
bunny_cleanpvdDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
bunny_cleanpvdDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
bunny_cleanpvdDisplay.PolarAxes.PolarTicksVisibility = 1
bunny_cleanpvdDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
bunny_cleanpvdDisplay.PolarAxes.TickLocation = 'Both'
bunny_cleanpvdDisplay.PolarAxes.AxisTickVisibility = 1
bunny_cleanpvdDisplay.PolarAxes.AxisMinorTickVisibility = 0
bunny_cleanpvdDisplay.PolarAxes.ArcTickVisibility = 1
bunny_cleanpvdDisplay.PolarAxes.ArcMinorTickVisibility = 0
bunny_cleanpvdDisplay.PolarAxes.DeltaAngleMajor = 10.0
bunny_cleanpvdDisplay.PolarAxes.DeltaAngleMinor = 5.0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
bunny_cleanpvdDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
bunny_cleanpvdDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
bunny_cleanpvdDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
bunny_cleanpvdDisplay.PolarAxes.ArcMajorTickSize = 0.0
bunny_cleanpvdDisplay.PolarAxes.ArcTickRatioSize = 0.3
bunny_cleanpvdDisplay.PolarAxes.ArcMajorTickThickness = 1.0
bunny_cleanpvdDisplay.PolarAxes.ArcTickRatioThickness = 0.5
bunny_cleanpvdDisplay.PolarAxes.Use2DMode = 0
bunny_cleanpvdDisplay.PolarAxes.UseLogAxis = 0

# show color bar/color legend
bunny_cleanpvdDisplay.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'f_5'
f_5TF2D = GetTransferFunction2D('f_5')

# turn off scalar coloring
ColorBy(bunny_cleanpvdDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(f_5LUT, renderView1)

# set active source
SetActiveSource(bunny_noisepvd)

# show data in view
bunny_noisepvdDisplay = Show(bunny_noisepvd, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
bunny_noisepvdDisplay.Selection = None
bunny_noisepvdDisplay.Representation = 'Surface'
bunny_noisepvdDisplay.ColorArrayName = ['CELLS', 'f_5']
bunny_noisepvdDisplay.LookupTable = f_5LUT
bunny_noisepvdDisplay.MapScalars = 1
bunny_noisepvdDisplay.MultiComponentsMapping = 0
bunny_noisepvdDisplay.InterpolateScalarsBeforeMapping = 1
bunny_noisepvdDisplay.Opacity = 1.0
bunny_noisepvdDisplay.PointSize = 2.0
bunny_noisepvdDisplay.LineWidth = 1.0
bunny_noisepvdDisplay.RenderLinesAsTubes = 0
bunny_noisepvdDisplay.RenderPointsAsSpheres = 0
bunny_noisepvdDisplay.Interpolation = 'Gouraud'
bunny_noisepvdDisplay.Specular = 0.0
bunny_noisepvdDisplay.SpecularColor = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.SpecularPower = 100.0
bunny_noisepvdDisplay.Luminosity = 0.0
bunny_noisepvdDisplay.Ambient = 0.0
bunny_noisepvdDisplay.Diffuse = 1.0
bunny_noisepvdDisplay.Roughness = 0.3
bunny_noisepvdDisplay.Metallic = 0.0
bunny_noisepvdDisplay.EdgeTint = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.Anisotropy = 0.0
bunny_noisepvdDisplay.AnisotropyRotation = 0.0
bunny_noisepvdDisplay.BaseIOR = 1.5
bunny_noisepvdDisplay.CoatStrength = 0.0
bunny_noisepvdDisplay.CoatIOR = 2.0
bunny_noisepvdDisplay.CoatRoughness = 0.0
bunny_noisepvdDisplay.CoatColor = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.SelectTCoordArray = 'None'
bunny_noisepvdDisplay.SelectNormalArray = 'None'
bunny_noisepvdDisplay.SelectTangentArray = 'None'
bunny_noisepvdDisplay.Texture = None
bunny_noisepvdDisplay.RepeatTextures = 1
bunny_noisepvdDisplay.InterpolateTextures = 0
bunny_noisepvdDisplay.SeamlessU = 0
bunny_noisepvdDisplay.SeamlessV = 0
bunny_noisepvdDisplay.UseMipmapTextures = 0
bunny_noisepvdDisplay.ShowTexturesOnBackface = 1
bunny_noisepvdDisplay.BaseColorTexture = None
bunny_noisepvdDisplay.NormalTexture = None
bunny_noisepvdDisplay.NormalScale = 1.0
bunny_noisepvdDisplay.CoatNormalTexture = None
bunny_noisepvdDisplay.CoatNormalScale = 1.0
bunny_noisepvdDisplay.MaterialTexture = None
bunny_noisepvdDisplay.OcclusionStrength = 1.0
bunny_noisepvdDisplay.AnisotropyTexture = None
bunny_noisepvdDisplay.EmissiveTexture = None
bunny_noisepvdDisplay.EmissiveFactor = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.FlipTextures = 0
bunny_noisepvdDisplay.BackfaceRepresentation = 'Follow Frontface'
bunny_noisepvdDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.BackfaceOpacity = 1.0
bunny_noisepvdDisplay.Position = [0.0, 0.0, 0.0]
bunny_noisepvdDisplay.Scale = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.Orientation = [0.0, 0.0, 0.0]
bunny_noisepvdDisplay.Origin = [0.0, 0.0, 0.0]
bunny_noisepvdDisplay.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
bunny_noisepvdDisplay.Pickable = 1
bunny_noisepvdDisplay.Triangulate = 0
bunny_noisepvdDisplay.UseShaderReplacements = 0
bunny_noisepvdDisplay.ShaderReplacements = ''
bunny_noisepvdDisplay.NonlinearSubdivisionLevel = 1
bunny_noisepvdDisplay.UseDataPartitions = 0
bunny_noisepvdDisplay.OSPRayUseScaleArray = 'All Approximate'
bunny_noisepvdDisplay.OSPRayScaleArray = ''
bunny_noisepvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
bunny_noisepvdDisplay.OSPRayMaterial = 'None'
bunny_noisepvdDisplay.BlockSelectors = ['/']
bunny_noisepvdDisplay.BlockColors = []
bunny_noisepvdDisplay.BlockOpacities = []
bunny_noisepvdDisplay.Orient = 0
bunny_noisepvdDisplay.OrientationMode = 'Direction'
bunny_noisepvdDisplay.SelectOrientationVectors = 'None'
bunny_noisepvdDisplay.Scaling = 0
bunny_noisepvdDisplay.ScaleMode = 'No Data Scaling Off'
bunny_noisepvdDisplay.ScaleFactor = 0.31240872957265386
bunny_noisepvdDisplay.SelectScaleArray = 'f_5'
bunny_noisepvdDisplay.GlyphType = 'Arrow'
bunny_noisepvdDisplay.UseGlyphTable = 0
bunny_noisepvdDisplay.GlyphTableIndexArray = 'f_5'
bunny_noisepvdDisplay.UseCompositeGlyphTable = 0
bunny_noisepvdDisplay.UseGlyphCullingAndLOD = 0
bunny_noisepvdDisplay.LODValues = []
bunny_noisepvdDisplay.ColorByLODIndex = 0
bunny_noisepvdDisplay.GaussianRadius = 0.015620436478632694
bunny_noisepvdDisplay.ShaderPreset = 'Sphere'
bunny_noisepvdDisplay.CustomTriangleScale = 3
bunny_noisepvdDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
bunny_noisepvdDisplay.Emissive = 0
bunny_noisepvdDisplay.ScaleByArray = 0
bunny_noisepvdDisplay.SetScaleArray = [None, '']
bunny_noisepvdDisplay.ScaleArrayComponent = 0
bunny_noisepvdDisplay.UseScaleFunction = 1
bunny_noisepvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
bunny_noisepvdDisplay.OpacityByArray = 0
bunny_noisepvdDisplay.OpacityArray = [None, '']
bunny_noisepvdDisplay.OpacityArrayComponent = 0
bunny_noisepvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
bunny_noisepvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
bunny_noisepvdDisplay.SelectionCellLabelBold = 0
bunny_noisepvdDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
bunny_noisepvdDisplay.SelectionCellLabelFontFamily = 'Arial'
bunny_noisepvdDisplay.SelectionCellLabelFontFile = ''
bunny_noisepvdDisplay.SelectionCellLabelFontSize = 18
bunny_noisepvdDisplay.SelectionCellLabelItalic = 0
bunny_noisepvdDisplay.SelectionCellLabelJustification = 'Left'
bunny_noisepvdDisplay.SelectionCellLabelOpacity = 1.0
bunny_noisepvdDisplay.SelectionCellLabelShadow = 0
bunny_noisepvdDisplay.SelectionPointLabelBold = 0
bunny_noisepvdDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
bunny_noisepvdDisplay.SelectionPointLabelFontFamily = 'Arial'
bunny_noisepvdDisplay.SelectionPointLabelFontFile = ''
bunny_noisepvdDisplay.SelectionPointLabelFontSize = 18
bunny_noisepvdDisplay.SelectionPointLabelItalic = 0
bunny_noisepvdDisplay.SelectionPointLabelJustification = 'Left'
bunny_noisepvdDisplay.SelectionPointLabelOpacity = 1.0
bunny_noisepvdDisplay.SelectionPointLabelShadow = 0
bunny_noisepvdDisplay.PolarAxes = 'PolarAxesRepresentation'
bunny_noisepvdDisplay.ScalarOpacityFunction = f_5PWF
bunny_noisepvdDisplay.ScalarOpacityUnitDistance = 0.12226345784296262
bunny_noisepvdDisplay.UseSeparateOpacityArray = 0
bunny_noisepvdDisplay.OpacityArrayName = ['CELLS', 'f_5']
bunny_noisepvdDisplay.OpacityComponent = ''
bunny_noisepvdDisplay.SelectMapper = 'Projected tetra'
bunny_noisepvdDisplay.SamplingDimensions = [128, 128, 128]
bunny_noisepvdDisplay.UseFloatingPointFrameBuffer = 1
bunny_noisepvdDisplay.SelectInputVectors = [None, '']
bunny_noisepvdDisplay.NumberOfSteps = 40
bunny_noisepvdDisplay.StepSize = 0.25
bunny_noisepvdDisplay.NormalizeVectors = 1
bunny_noisepvdDisplay.EnhancedLIC = 1
bunny_noisepvdDisplay.ColorMode = 'Blend'
bunny_noisepvdDisplay.LICIntensity = 0.8
bunny_noisepvdDisplay.MapModeBias = 0.0
bunny_noisepvdDisplay.EnhanceContrast = 'Off'
bunny_noisepvdDisplay.LowLICContrastEnhancementFactor = 0.0
bunny_noisepvdDisplay.HighLICContrastEnhancementFactor = 0.0
bunny_noisepvdDisplay.LowColorContrastEnhancementFactor = 0.0
bunny_noisepvdDisplay.HighColorContrastEnhancementFactor = 0.0
bunny_noisepvdDisplay.AntiAlias = 0
bunny_noisepvdDisplay.MaskOnSurface = 1
bunny_noisepvdDisplay.MaskThreshold = 0.0
bunny_noisepvdDisplay.MaskIntensity = 0.0
bunny_noisepvdDisplay.MaskColor = [0.5, 0.5, 0.5]
bunny_noisepvdDisplay.GenerateNoiseTexture = 0
bunny_noisepvdDisplay.NoiseType = 'Gaussian'
bunny_noisepvdDisplay.NoiseTextureSize = 128
bunny_noisepvdDisplay.NoiseGrainSize = 2
bunny_noisepvdDisplay.MinNoiseValue = 0.0
bunny_noisepvdDisplay.MaxNoiseValue = 0.8
bunny_noisepvdDisplay.NumberOfNoiseLevels = 1024
bunny_noisepvdDisplay.ImpulseNoiseProbability = 1.0
bunny_noisepvdDisplay.ImpulseNoiseBackgroundValue = 0.0
bunny_noisepvdDisplay.NoiseGeneratorSeed = 1
bunny_noisepvdDisplay.CompositeStrategy = 'AUTO'
bunny_noisepvdDisplay.UseLICForLOD = 0
bunny_noisepvdDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
bunny_noisepvdDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
bunny_noisepvdDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
bunny_noisepvdDisplay.GlyphType.TipResolution = 6
bunny_noisepvdDisplay.GlyphType.TipRadius = 0.1
bunny_noisepvdDisplay.GlyphType.TipLength = 0.35
bunny_noisepvdDisplay.GlyphType.ShaftResolution = 6
bunny_noisepvdDisplay.GlyphType.ShaftRadius = 0.03
bunny_noisepvdDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
bunny_noisepvdDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
bunny_noisepvdDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
bunny_noisepvdDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
bunny_noisepvdDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
bunny_noisepvdDisplay.DataAxesGrid.XTitle = 'X Axis'
bunny_noisepvdDisplay.DataAxesGrid.YTitle = 'Y Axis'
bunny_noisepvdDisplay.DataAxesGrid.ZTitle = 'Z Axis'
bunny_noisepvdDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
bunny_noisepvdDisplay.DataAxesGrid.XTitleFontFile = ''
bunny_noisepvdDisplay.DataAxesGrid.XTitleBold = 0
bunny_noisepvdDisplay.DataAxesGrid.XTitleItalic = 0
bunny_noisepvdDisplay.DataAxesGrid.XTitleFontSize = 12
bunny_noisepvdDisplay.DataAxesGrid.XTitleShadow = 0
bunny_noisepvdDisplay.DataAxesGrid.XTitleOpacity = 1.0
bunny_noisepvdDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
bunny_noisepvdDisplay.DataAxesGrid.YTitleFontFile = ''
bunny_noisepvdDisplay.DataAxesGrid.YTitleBold = 0
bunny_noisepvdDisplay.DataAxesGrid.YTitleItalic = 0
bunny_noisepvdDisplay.DataAxesGrid.YTitleFontSize = 12
bunny_noisepvdDisplay.DataAxesGrid.YTitleShadow = 0
bunny_noisepvdDisplay.DataAxesGrid.YTitleOpacity = 1.0
bunny_noisepvdDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
bunny_noisepvdDisplay.DataAxesGrid.ZTitleFontFile = ''
bunny_noisepvdDisplay.DataAxesGrid.ZTitleBold = 0
bunny_noisepvdDisplay.DataAxesGrid.ZTitleItalic = 0
bunny_noisepvdDisplay.DataAxesGrid.ZTitleFontSize = 12
bunny_noisepvdDisplay.DataAxesGrid.ZTitleShadow = 0
bunny_noisepvdDisplay.DataAxesGrid.ZTitleOpacity = 1.0
bunny_noisepvdDisplay.DataAxesGrid.FacesToRender = 63
bunny_noisepvdDisplay.DataAxesGrid.CullBackface = 0
bunny_noisepvdDisplay.DataAxesGrid.CullFrontface = 1
bunny_noisepvdDisplay.DataAxesGrid.ShowGrid = 0
bunny_noisepvdDisplay.DataAxesGrid.ShowEdges = 1
bunny_noisepvdDisplay.DataAxesGrid.ShowTicks = 1
bunny_noisepvdDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
bunny_noisepvdDisplay.DataAxesGrid.AxesToLabel = 63
bunny_noisepvdDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
bunny_noisepvdDisplay.DataAxesGrid.XLabelFontFile = ''
bunny_noisepvdDisplay.DataAxesGrid.XLabelBold = 0
bunny_noisepvdDisplay.DataAxesGrid.XLabelItalic = 0
bunny_noisepvdDisplay.DataAxesGrid.XLabelFontSize = 12
bunny_noisepvdDisplay.DataAxesGrid.XLabelShadow = 0
bunny_noisepvdDisplay.DataAxesGrid.XLabelOpacity = 1.0
bunny_noisepvdDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
bunny_noisepvdDisplay.DataAxesGrid.YLabelFontFile = ''
bunny_noisepvdDisplay.DataAxesGrid.YLabelBold = 0
bunny_noisepvdDisplay.DataAxesGrid.YLabelItalic = 0
bunny_noisepvdDisplay.DataAxesGrid.YLabelFontSize = 12
bunny_noisepvdDisplay.DataAxesGrid.YLabelShadow = 0
bunny_noisepvdDisplay.DataAxesGrid.YLabelOpacity = 1.0
bunny_noisepvdDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
bunny_noisepvdDisplay.DataAxesGrid.ZLabelFontFile = ''
bunny_noisepvdDisplay.DataAxesGrid.ZLabelBold = 0
bunny_noisepvdDisplay.DataAxesGrid.ZLabelItalic = 0
bunny_noisepvdDisplay.DataAxesGrid.ZLabelFontSize = 12
bunny_noisepvdDisplay.DataAxesGrid.ZLabelShadow = 0
bunny_noisepvdDisplay.DataAxesGrid.ZLabelOpacity = 1.0
bunny_noisepvdDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
bunny_noisepvdDisplay.DataAxesGrid.XAxisPrecision = 2
bunny_noisepvdDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
bunny_noisepvdDisplay.DataAxesGrid.XAxisLabels = []
bunny_noisepvdDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
bunny_noisepvdDisplay.DataAxesGrid.YAxisPrecision = 2
bunny_noisepvdDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
bunny_noisepvdDisplay.DataAxesGrid.YAxisLabels = []
bunny_noisepvdDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
bunny_noisepvdDisplay.DataAxesGrid.ZAxisPrecision = 2
bunny_noisepvdDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
bunny_noisepvdDisplay.DataAxesGrid.ZAxisLabels = []
bunny_noisepvdDisplay.DataAxesGrid.UseCustomBounds = 0
bunny_noisepvdDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
bunny_noisepvdDisplay.PolarAxes.Visibility = 0
bunny_noisepvdDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
bunny_noisepvdDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
bunny_noisepvdDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
bunny_noisepvdDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
bunny_noisepvdDisplay.PolarAxes.EnableCustomRange = 0
bunny_noisepvdDisplay.PolarAxes.CustomRange = [0.0, 1.0]
bunny_noisepvdDisplay.PolarAxes.PolarAxisVisibility = 1
bunny_noisepvdDisplay.PolarAxes.RadialAxesVisibility = 1
bunny_noisepvdDisplay.PolarAxes.DrawRadialGridlines = 1
bunny_noisepvdDisplay.PolarAxes.PolarArcsVisibility = 1
bunny_noisepvdDisplay.PolarAxes.DrawPolarArcsGridlines = 1
bunny_noisepvdDisplay.PolarAxes.NumberOfRadialAxes = 0
bunny_noisepvdDisplay.PolarAxes.AutoSubdividePolarAxis = 1
bunny_noisepvdDisplay.PolarAxes.NumberOfPolarAxis = 0
bunny_noisepvdDisplay.PolarAxes.MinimumRadius = 0.0
bunny_noisepvdDisplay.PolarAxes.MinimumAngle = 0.0
bunny_noisepvdDisplay.PolarAxes.MaximumAngle = 90.0
bunny_noisepvdDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
bunny_noisepvdDisplay.PolarAxes.Ratio = 1.0
bunny_noisepvdDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
bunny_noisepvdDisplay.PolarAxes.PolarAxisTitleVisibility = 1
bunny_noisepvdDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
bunny_noisepvdDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
bunny_noisepvdDisplay.PolarAxes.PolarLabelVisibility = 1
bunny_noisepvdDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
bunny_noisepvdDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
bunny_noisepvdDisplay.PolarAxes.RadialLabelVisibility = 1
bunny_noisepvdDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
bunny_noisepvdDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
bunny_noisepvdDisplay.PolarAxes.RadialUnitsVisibility = 1
bunny_noisepvdDisplay.PolarAxes.ScreenSize = 10.0
bunny_noisepvdDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
bunny_noisepvdDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
bunny_noisepvdDisplay.PolarAxes.PolarAxisTitleFontFile = ''
bunny_noisepvdDisplay.PolarAxes.PolarAxisTitleBold = 0
bunny_noisepvdDisplay.PolarAxes.PolarAxisTitleItalic = 0
bunny_noisepvdDisplay.PolarAxes.PolarAxisTitleShadow = 0
bunny_noisepvdDisplay.PolarAxes.PolarAxisTitleFontSize = 12
bunny_noisepvdDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
bunny_noisepvdDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
bunny_noisepvdDisplay.PolarAxes.PolarAxisLabelFontFile = ''
bunny_noisepvdDisplay.PolarAxes.PolarAxisLabelBold = 0
bunny_noisepvdDisplay.PolarAxes.PolarAxisLabelItalic = 0
bunny_noisepvdDisplay.PolarAxes.PolarAxisLabelShadow = 0
bunny_noisepvdDisplay.PolarAxes.PolarAxisLabelFontSize = 12
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisTextBold = 0
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisTextItalic = 0
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisTextShadow = 0
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
bunny_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
bunny_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
bunny_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
bunny_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
bunny_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
bunny_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
bunny_noisepvdDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
bunny_noisepvdDisplay.PolarAxes.EnableDistanceLOD = 1
bunny_noisepvdDisplay.PolarAxes.DistanceLODThreshold = 0.7
bunny_noisepvdDisplay.PolarAxes.EnableViewAngleLOD = 1
bunny_noisepvdDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
bunny_noisepvdDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
bunny_noisepvdDisplay.PolarAxes.PolarTicksVisibility = 1
bunny_noisepvdDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
bunny_noisepvdDisplay.PolarAxes.TickLocation = 'Both'
bunny_noisepvdDisplay.PolarAxes.AxisTickVisibility = 1
bunny_noisepvdDisplay.PolarAxes.AxisMinorTickVisibility = 0
bunny_noisepvdDisplay.PolarAxes.ArcTickVisibility = 1
bunny_noisepvdDisplay.PolarAxes.ArcMinorTickVisibility = 0
bunny_noisepvdDisplay.PolarAxes.DeltaAngleMajor = 10.0
bunny_noisepvdDisplay.PolarAxes.DeltaAngleMinor = 5.0
bunny_noisepvdDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
bunny_noisepvdDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
bunny_noisepvdDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
bunny_noisepvdDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
bunny_noisepvdDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
bunny_noisepvdDisplay.PolarAxes.ArcMajorTickSize = 0.0
bunny_noisepvdDisplay.PolarAxes.ArcTickRatioSize = 0.3
bunny_noisepvdDisplay.PolarAxes.ArcMajorTickThickness = 1.0
bunny_noisepvdDisplay.PolarAxes.ArcTickRatioThickness = 0.5
bunny_noisepvdDisplay.PolarAxes.Use2DMode = 0
bunny_noisepvdDisplay.PolarAxes.UseLogAxis = 0

# show color bar/color legend
bunny_noisepvdDisplay.SetScalarBarVisibility(renderView1, True)

# turn off scalar coloring
ColorBy(bunny_noisepvdDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(f_5LUT, renderView1)

# hide data in view
Hide(classicxdmf, renderView1)

# hide data in view
Hide(bunny_cleanpvd, renderView1)

# set active source
SetActiveSource(bunny_cleanpvd)

# show data in view
bunny_cleanpvdDisplay = Show(bunny_cleanpvd, renderView1, 'UnstructuredGridRepresentation')

# hide data in view
Hide(bunny_noisepvd, renderView1)

# set active source
SetActiveSource(classicxdmf)

# show data in view
classicxdmfDisplay = Show(classicxdmf, renderView1, 'UnstructuredGridRepresentation')

# hide data in view
Hide(bunny_cleanpvd, renderView1)

animationScene1.GoToLast()

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
renderView1.CameraPosition = [-4.5091241011134, 3.067029232561387, 6.560408447704282]
renderView1.CameraFocalPoint = [-0.33664774894714294, 1.20539477467537, -0.03465276956558295]
renderView1.CameraViewUp = [0.04938571052357882, 0.9689516068478651, -0.24226810599627369]
renderView1.CameraParallelScale = 2.5126014486894097

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
