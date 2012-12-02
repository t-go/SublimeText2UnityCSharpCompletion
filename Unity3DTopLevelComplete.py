import sublime, sublime_plugin

class Unity3DTopLevelComplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
    	if not view.file_name().endswith('.cs'):
			return []
	
	result = []
	if view.find('using[\s]*AOT;',0):
		result.extend(AOT)
	
	if view.find('using[\s]*UnityEngine;',0):
		result.extend(UNITYENGINE)

		if view.find('using[\s]*UnityEngine.Flash;',0):
			result.extend(UNITYENGINE_FLASH)

		if view.find('using[\s]*UnityEngine.Serialization;',0):
			result.extend(UNITYENGINE_SERIALIZATION)

		if view.find('using[\s]*UnityEngine.SocialPlatforms;',0):
			result.extend(UNITYENGINE_SOCIALPLATFORMS)

			if view.find('using[\s]*UnityEngine.SocialPlatforms.Gamecenter;',0):
				result.extend(UNITYENGINE_SOCIALPLATFORMS_GAMECENTER)

			if view.find('using[\s]*UnityEngine.SocialPlatforms.Impl;',0):
				result.extend(UNITYENGINE_SOCIALPLATFORMS_IMPLE)

	if view.find('using[\s]*UnityEngineInternal;',0):
		result.extend(UNITYENGINEINTERNAL)



	if view.find('using[\s]*TreeEditor;',0):	
		result.extend(TREEEDITOR)

	if view.find('using[\s]*UnityEditor;',0):	
		result.extend(UNITYEDITOR)

		if view.find('using[\s]*UnityEditor.Callbacks;',0):	
			result.extend(UNITYEDITOR_CALLBACKS)
	
		if view.find('using[\s]*UnityEditor.Macros;',0):	
			result.extend(UNITYEDITOR_MACROS)
	
		if view.find('using[\s]*UnityEditor.VisualStudioIntegration;',0):	
			result.extend(UNITYEDITOR_VISUALSTUDIOINTEGRATION)
	
	if view.find('using[\s]*UnityEditorInternal;',0):	
		result.extend(UNITYEDITORINTERNAL)


        return result


UNITYENGINE =[
				('ADBannerView','ADBannerView'),
				('ADError','ADError'),
				('ADInterstitialAd','ADInterstitialAd'),
				('AccelerationEvent','AccelerationEvent'),
				('AndroidInput','AndroidInput'),
				('AndroidJNIHelper','AndroidJNIHelper'),
				('AndroidJNI','AndroidJNI'),
				('AndroidJavaObject','AndroidJavaObject'),
				('AndroidJavaClass','AndroidJavaClass'),
				('AnimationClip','AnimationClip'),
				('AnimationCurve','AnimationCurve'),
				('AnimationEvent','AnimationEvent'),
				('AnimationInfo','AnimationInfo'),
				('AnimationState','AnimationState'),
				('AnimatorStateInfo','AnimatorStateInfo'),
				('AnimatorTransitionInfo','AnimatorTransitionInfo'),
				('Application','Application'),
				('Array','Array'),
				('AudioSettings','AudioSettings'),
				('BitStream','BitStream'),
				('BoneWeight','BoneWeight'),
				('Bounds','Bounds'),
				('Caching','Caching'),
				('CharacterInfo','CharacterInfo'),
				('ClothSkinningCoefficient','ClothSkinningCoefficient'),
				('Collision','Collision'),
				('Color32','Color32'),
				('Color','Color'),
				('CombineInstance','CombineInstance'),
				('Compass','Compass'),
				('ComputeBuffer','ComputeBuffer'),
				('ContactPoint','ContactPoint'),
				('ControllerColliderHit','ControllerColliderHit'),
				('Cursor','Cursor'),
				('Debug','Debug'),
				('DetailPrototype','DetailPrototype'),
				('Event','Event'),
				('GL','GL'),
				('GUIContent','GUIContent'),
				('GUILayoutOption','GUILayoutOption'),
				('GUILayoutUtility','GUILayoutUtility'),
				('GUILayout','GUILayout'),
				('GUISettings','GUISettings'),
				('GUIStyleState','GUIStyleState'),
				('GUIStyle','GUIStyle'),
				('GUIUtility','GUIUtility'),
				('GUI','GUI'),
				('GeometryUtility','GeometryUtility'),
				('Gizmos','Gizmos'),
				('GradientAlphaKey','GradientAlphaKey'),
				('GradientColorKey','GradientColorKey'),
				('Gradient','Gradient'),
				('Graphics','Graphics'),
				('Gyroscope','Gyroscope'),
				('Handheld','Handheld'),
				('Hashtable','Hashtable'),
				('HostData','HostData'),
				('Input','Input'),
				('JointDrive','JointDrive'),
				('JointLimits','JointLimits'),
				('JointMotor','JointMotor'),
				('JointSpring','JointSpring'),
				('Keyframe','Keyframe'),
				('LOD','LOD'),
				('LayerMask','LayerMask'),
				('LightmapData','LightmapData'),
				('LightmapSettings','LightmapSettings'),
				('LocalNotification','LocalNotification'),
				('LocationInfo','LocationInfo'),
				('LocationService','LocationService'),
				('MasterServer','MasterServer'),
				('MatchTargetWeightMask','MatchTargetWeightMask'),
				('MaterialPropertyBlock','MaterialPropertyBlock'),
				('Mathf','Mathf'),
				('Matrix4x4','Matrix4x4'),
				('Microphone','Microphone'),
				('NavMeshHit','NavMeshHit'),
				('NavMeshPath','NavMeshPath'),
				('NetworkMessageInfo','NetworkMessageInfo'),
				('NetworkPlayer','NetworkPlayer'),
				('NetworkViewID','NetworkViewID'),
				('Network','Network'),
				('NotificationServices','NotificationServices'),
				('Object','Object'),
				('AssetBundle','AssetBundle'),
				('AudioClip','AudioClip'),
				('Avatar','Avatar'),
				('Component','Component'),
				('Behaviour','Behaviour'),
				('Animation','Animation'),
				('Animator','Animator'),
				('AudioChorusFilter','AudioChorusFilter'),
				('AudioDistortionFilter','AudioDistortionFilter'),
				('AudioEchoFilter','AudioEchoFilter'),
				('AudioHighPassFilter','AudioHighPassFilter'),
				('AudioListener','AudioListener'),
				('AudioLowPassFilter','AudioLowPassFilter'),
				('AudioReverbFilter','AudioReverbFilter'),
				('AudioReverbZone','AudioReverbZone'),
				('AudioSource','AudioSource'),
				('Camera','Camera'),
				('ConstantForce','ConstantForce'),
				('GUIElement','GUIElement'),
				('GUIText','GUIText'),
				('GUITexture','GUITexture'),
				('GUILayer','GUILayer'),
				('LensFlare','LensFlare'),
				('Light','Light'),
				('MonoBehaviour','MonoBehaviour'),
				('Terrain','Terrain'),
				('NavMeshAgent','NavMeshAgent'),
				('NavMeshObstacle','NavMeshObstacle'),
				('NetworkView','NetworkView'),
				('Projector','Projector'),
				('Skybox','Skybox'),
				('Cloth','Cloth'),
				('InteractiveCloth','InteractiveCloth'),
				('SkinnedCloth','SkinnedCloth'),
				('Collider','Collider'),
				('BoxCollider','BoxCollider'),
				('CapsuleCollider','CapsuleCollider'),
				('CharacterController','CharacterController'),
				('MeshCollider','MeshCollider'),
				('SphereCollider','SphereCollider'),
				('TerrainCollider','TerrainCollider'),
				('WheelCollider','WheelCollider'),
				('Joint','Joint'),
				('CharacterJoint','CharacterJoint'),
				('ConfigurableJoint','ConfigurableJoint'),
				('FixedJoint','FixedJoint'),
				('HingeJoint','HingeJoint'),
				('SpringJoint','SpringJoint'),
				('LODGroup','LODGroup'),
				('LightProbeGroup','LightProbeGroup'),
				('MeshFilter','MeshFilter'),
				('OcclusionArea','OcclusionArea'),
				('OcclusionPortal','OcclusionPortal'),
				('OffMeshLink','OffMeshLink'),
				('ParticleAnimator','ParticleAnimator'),
				('ParticleEmitter','ParticleEmitter'),
				('ParticleSystem','ParticleSystem'),
				('Renderer','Renderer'),
				('ClothRenderer','ClothRenderer'),
				('LineRenderer','LineRenderer'),
				('MeshRenderer','MeshRenderer'),
				('ParticleRenderer','ParticleRenderer'),
				('ParticleSystemRenderer','ParticleSystemRenderer'),
				('SkinnedMeshRenderer','SkinnedMeshRenderer'),
				('TrailRenderer','TrailRenderer'),
				('Rigidbody','Rigidbody'),
				('TextMesh','TextMesh'),
				('Transform','Transform'),
				('Tree','Tree'),
				('ComputeShader','ComputeShader'),
				('Flare','Flare'),
				('Font','Font'),
				('GameObject','GameObject'),
				('LightProbes','LightProbes'),
				('Material','Material'),
				('ProceduralMaterial','ProceduralMaterial'),
				('Mesh','Mesh'),
				('NavMesh','NavMesh'),
				('PhysicMaterial','PhysicMaterial'),
				('QualitySettings','QualitySettings'),
				('RenderSettings','RenderSettings'),
				('ScriptableObject','ScriptableObject'),
				('GUISkin','GUISkin'),
				('Shader','Shader'),
				('TerrainData','TerrainData'),
				('TextAsset','TextAsset'),
				('Texture','Texture'),
				('Cubemap','Cubemap'),
				('MovieTexture','MovieTexture'),
				('RenderTexture','RenderTexture'),
				('Texture2D','Texture2D'),
				('Texture3D','Texture3D'),
				('WebCamTexture','WebCamTexture'),
				('OffMeshLinkData','OffMeshLinkData'),
				('ParticleSystem.Particle','ParticleSystem.Particle'),
				('Particle','Particle'),
				('Path','Path'),
				('Physics','Physics'),
				('Ping','Ping'),
				('Plane','Plane'),
				('PlayerPrefsException','PlayerPrefsException'),
				('PlayerPrefs','PlayerPrefs'),
				('ProceduralPropertyDescription','ProceduralPropertyDescription'),
				('Profiler','Profiler'),
				('Quaternion','Quaternion'),
				('Random','Random'),		
				('Ray','Ray'),
				('RaycastHit','RaycastHit'),
				('RectOffset','RectOffset'),
				('Rect','Rect'),
				('RemoteNotification','RemoteNotification'),
				('RenderBuffer','RenderBuffer'),
				('Resolution','Resolution'),
				('Resources','Resources'),
				('Screen','Screen'),
				('Security','Security'),
				('SleepTimeout','SleepTimeout'),
				('Social','Social'),
				('SoftJointLimit','SoftJointLimit'),
				('SplatPrototype','SplatPrototype'),
				('StaticBatchingUtility','StaticBatchingUtility'),
				('String','String'),
				('SystemInfo','SystemInfo'),
				('Time','Time'),
				('TouchScreenKeyboard','TouchScreenKeyboard'),
				('Touch','Touch'),
				('TreeInstance','TreeInstance'),
				('TreePrototype','TreePrototype'),
				('Vector2','Vector2'),
				('Vector3','Vector3'),
				('Vector4','Vector4'),
				('WWWForm','WWWForm'),
				('WWW','WWW'),
				('WebCamDevice','WebCamDevice'),
				('WheelFrictionCurve','WheelFrictionCurve'),
				('WheelHit','WheelHit'),
				('YieldInstruction','YieldInstruction'),
				('AsyncOperation','AsyncOperation'),
				('AssetBundleCreateRequest','AssetBundleCreateRequest'),
				('AssetBundleRequest','AssetBundleRequest'),
				('Coroutine','Coroutine'),
				('WaitForEndOfFrame','WaitForEndOfFrame'),
				('WaitForFixedUpdate','WaitForFixedUpdate'),
				('WaitForSeconds','WaitForSeconds'),
				('iPhoneInput','iPhoneInput'),
				('iPhoneSettings','iPhoneSettings'),
				('iPhoneUtils','iPhoneUtils'),
				('iPhone','iPhone'),
				# enum
				('ADErrorCode','ADErrorCode'),
				('ADPosition','ADPosition'),
				('ADSizeIdentifier','ADSizeIdentifier'),
				('AndroidActivityIndicatorStyle','AndroidActivityIndicatorStyle'),
				('AnimationBlendMode','AnimationBlendMode'),
				('AnimationCullingType','AnimationCullingType'),
				('AnimatorCullingMode','AnimatorCullingMode'),
				('AnisotropicFiltering','AnisotropicFiltering'),
				('AudioReverbPreset','AudioReverbPreset'),
				('AudioRolloffMode','AudioRolloffMode'),
				('AudioSpeakerMode','AudioSpeakerMode'),
				('AudioType','AudioType'),
				('AudioVelocityUpdateMode','AudioVelocityUpdateMode'),
				('AvatarIKGoal','AvatarIKGoal'),
				('AvatarTarget','AvatarTarget'),
				('BlendWeights','BlendWeights'),
				('CalendarIdentifier','CalendarIdentifier'),
				('CalendarUnit','CalendarUnit'),
				('CameraClearFlags','CameraClearFlags'),
				('CollisionDetectionMode','CollisionDetectionMode'),
				('CollisionFlags','CollisionFlags'),
				('ColorSpace','ColorSpace'),
				('ComputeBufferType','ComputeBufferType'),
				('ConfigurableJointMotion','ConfigurableJointMotion'),
				('ConnectionTesterStatus','ConnectionTesterStatus'),
				('CubemapFace','CubemapFace'),
				('CursorMode','CursorMode'),
				('DepthTextureMode','DepthTextureMode'),
				('DetailRenderMode','DetailRenderMode'),
				('DeviceOrientation','DeviceOrientation'),
				('DeviceType','DeviceType'),
				('EventModifiers','EventModifiers'),
				('EventType','EventType'),
				('FFTWindow','FFTWindow'),
				('FilterMode','FilterMode'),
				('FocusType','FocusType'),
				('FogMode','FogMode'),
				('FontStyle','FontStyle'),
				('ForceMode','ForceMode'),
				('FullScreenMovieControlMode','FullScreenMovieControlMode'),
				('FullScreenMovieScalingMode','FullScreenMovieScalingMode'),
				('HideFlags','HideFlags'),
				('HumanBodyBones','HumanBodyBones'),
				('IMECompositionMode','IMECompositionMode'),
				('ImagePosition','ImagePosition'),
				('JointDriveMode','JointDriveMode'),
				('JointProjectionMode','JointProjectionMode'),
				('KeyCode','KeyCode'),
				('LightRenderMode','LightRenderMode'),
				('LightShadows','LightShadows'),
				('LightType','LightType'),
				('LightmapsMode','LightmapsMode'),
				('LocationServiceStatus','LocationServiceStatus'),
				('LogType','LogType'),
				('MasterServerEvent','MasterServerEvent'),
				('MeshTopology','MeshTopology'),
				('NavMeshPathStatus','NavMeshPathStatus'),
				('NetworkConnectionError','NetworkConnectionError'),
				('NetworkDisconnection','NetworkDisconnection'),
				('NetworkLogLevel','NetworkLogLevel'),
				('NetworkPeerType','NetworkPeerType'),
				('NetworkReachability','NetworkReachability'),
				('NetworkStateSynchronization','NetworkStateSynchronization'),
				('ObstacleAvoidanceType','ObstacleAvoidanceType'),
				('OffMeshLinkType','OffMeshLinkType'),
				('ParticleRenderMode','ParticleRenderMode'),
				('ParticleSystemRenderMode','ParticleSystemRenderMode'),
				('PhysicMaterialCombine','PhysicMaterialCombine'),
				('PlayMode','PlayMode'),
				('PrimitiveType','PrimitiveType'),
				('ProceduralCacheSize','ProceduralCacheSize'),
				('ProceduralLoadingBehavior','ProceduralLoadingBehavior'),
				('ProceduralProcessorUsage','ProceduralProcessorUsage'),
				('ProceduralPropertyType','ProceduralPropertyType'),
				('QueueMode','QueueMode'),
				('RPCMode','RPCMode'),
				('RemoteNotificationType','RemoteNotificationType'),
				('RenderTextureFormat','RenderTextureFormat'),
				('RenderTextureReadWrite','RenderTextureReadWrite'),
				('RenderingPath','RenderingPath'),
				('RigidbodyConstraints','RigidbodyConstraints'),
				('RigidbodyInterpolation','RigidbodyInterpolation'),
				('RotationDriveMode','RotationDriveMode'),
				('RuntimePlatform','RuntimePlatform'),
				('ScaleMode','ScaleMode'),
				('ScreenOrientation','ScreenOrientation'),
				('SendMessageOptions','SendMessageOptions'),
				('ShadowProjection','ShadowProjection'),
				('SkinQuality','SkinQuality'),
				('Space','Space'),
				('SystemLanguage','SystemLanguage'),
				('TerrainRenderFlags','TerrainRenderFlags'),
				('TextAlignment','TextAlignment'),
				('TextAnchor','TextAnchor'),
				('TextClipping','TextClipping'),
				('TextureCompressionQuality','TextureCompressionQuality'),
				('TextureFormat','TextureFormat'),
				('TextureWrapMode','TextureWrapMode'),
				('ThreadPriority','ThreadPriority'),
				('TimeScope','TimeScope'),
				('TouchPhase','TouchPhase'),
				('TouchScreenKeyboardType','TouchScreenKeyboardType'),
				('TransparencySortMode','TransparencySortMode'),
				('UserAuthorization','UserAuthorization'),
				('UserScope','UserScope'),
				('UserState','UserState'),
				('WiiUtils.LoadingScreen.Placement','WiiUtils.LoadingScreen.Placement'),
				('WrapMode','WrapMode'),
				('iOSActivityIndicatorStyle','iOSActivityIndicatorStyle'),
				('iPhoneGeneration','iPhoneGeneration')
]

AOT = [
				('MonoPInvokeCallbackAttribute','MonoPInvokeCallback')
]
UNITYENGINE_FLASH = [
				('ActionScript','ActionScript'),
				('FlashPlayer','FlashPlayer'),
]
UNITYENGINE_SERIALIZATION = [
				('UnitySurrogateSelector','UnitySurrogateSelector')
]
UNITYENGINE_SOCIALPLATFORMS = [
				('IAchievementDescription','IAchievementDescription'),
				('IAchievement','IAchievement'),
				('ILeaderboard','ILeaderboard'),
				('IScore','IScore'),
				('ISocialPlatform','ISocialPlatform'),
				('IUserProfile','IUserProfile'),
				('ILocalUser','ILocalUser'),
				('Local','Local'),
				('Range','Range'),
				# enum
				('TimeScope','TimeScope'),
				('UserScope', 'UserScope'),
				('UserState', 'UserState')
]
UNITYENGINE_SOCIALPLATFORMS_GAMECENTER = [
				('GameCenterPlatform','GameCenterPlatform')
]
UNITYENGINE_SOCIALPLATFORMS_IMPLE = [
				('AchievementDescription','AchievementDescription'),
				('Achievement','Achievement'),
				('Leaderboard','Leaderboard'),
				('Score','Score'),
				('UserProfile','UserProfile'),
				('LocalUser','LocalUser'),
]
UNITYENGINEINTERNAL = [
				('Reproduction','Reproduction'),
				('TypeInferenceRuleAttribute','TypeInferenceRule'),
				# enum
				('TypeInferenceRules','TypeInferenceRules')
]

UNITYEDITOR = [
				('AnimationClipCurveData','AnimationClipCurveData'),
				('AnimationUtility','AnimationUtility'),
				('ArrayUtility','ArrayUtility'),
				('AssetDatabase','AssetDatabase'),
				('AssetImporter','AssetImporter'),
				('AudioImporter','AudioImporter'),
				('ModelImporter','ModelImporter'),
				('MonoImporter','MonoImporter'),
				('MovieImporter','MovieImporter'),
				('SubstanceImporter','SubstanceImporter'),
				('TextureImporter','TextureImporter'),
				('TrueTypeFontImporter','TrueTypeFontImporter'),
				('AssetModificationProcessor','AssetModificationProcessor'),
				('AssetPostprocessor','AssetPostprocessor'),
				('AssetPreview','AssetPreview'),
				('AssetStoreToolUtils','AssetStoreToolUtils'),
				('AssetStore','AssetStore'),
				('BuildPipeline','BuildPipeline'),
				('DragAndDrop','DragAndDrop'),
				('EditorApplication','EditorApplication'),
				('EditorBuildSettings','EditorBuildSettings'),
				('EditorGUILayout','EditorGUILayout'),
				('EditorGUIUtility','EditorGUIUtility'),
				('EditorGUI','EditorGUI'),
				('EditorPrefs','EditorPrefs'),
				('EditorStyles','EditorStyles'),
				('EditorUserBuildSettings','EditorUserBuildSettings'),
				('EditorUtility','EditorUtility'),
				('EditorWindow','EditorWindow'),
				('ScriptableWizard','ScriptableWizard'),
				('Editor','Editor'),
				('FileUtil','FileUtil'),
				('GameObjectUtility','GameObjectUtility'),
				('GenericMenu','GenericMenu'),
				('HandleUtility','HandleUtility'),
				('Handles','Handles'),
				('Help','Help'),
				('LODUtility','LODUtility'),
				('LightmapEditorSettings','LightmapEditorSettings'),
				('Lightmapping','Lightmapping'),
				('MenuCommand','MenuCommand'),
				('MeshUtility','MeshUtility'),
				('ModelImporterClipAnimation','ModelImporterClipAnimation'),
				('MonoScript','MonoScript'),
				('NavMeshBuilder','NavMeshBuilder'),
				('ObjectNames','ObjectNames'),
				('PlayerSettings.Android','PlayerSettings.Android'),
				('PlayerSettings.Wii','PlayerSettings.Wii'),
				('PlayerSettings.iOS','PlayerSettings.iOS'),
				('PlayerSettings','PlayerSettings'),
				('PrefabUtility','PrefabUtility'),
				('ProceduralTexture','ProceduralTexture'),
				('PropertyDrawer','PropertyDrawer'),
				('PropertyModification','PropertyModification'),
				('Selection','Selection'),
				('SerializedObject','SerializedObject'),
				('SerializedProperty','SerializedProperty'),
				('StaticOcclusionCullingVisualization','StaticOcclusionCullingVisualization'),
				('StaticOcclusionCulling','StaticOcclusionCulling'),
				('SubstanceArchive','SubstanceArchive'),
				('TextureImporterSettings','TextureImporterSettings'),
				('Tools','Tools'),
				('Undo','Undo'),
				('UnwrapParam','UnwrapParam'),
				('Unwrapping','Unwrapping'),
				# enum
				('AndroidBuildSubtarget','AndroidBuildSubtarget'),
				('AndroidPreferredInstallLocation','AndroidPreferredInstallLocation'),
				('AndroidSdkVersions','AndroidSdkVersions'),
				('AndroidShowActivityIndicatorOnLoading','AndroidShowActivityIndicatorOnLoading'),
				('AndroidSplashScreenScale','AndroidSplashScreenScale'),
				('AndroidTargetDevice','AndroidTargetDevice'),
				('ApiCompatibilityLevel','ApiCompatibilityLevel'),
				('AspectRatio','AspectRatio'),
				('AssetDeleteResult','AssetDeleteResult'),
				('AssetMoveResult','AssetMoveResult'),
				('AudioImporterFormat','AudioImporterFormat'),
				('AudioImporterLoadType','AudioImporterLoadType'),
				('BuildAssetBundleOptions','BuildAssetBundleOptions'),
				('BuildOptions','BuildOptions'),
				('BuildTargetGroup','BuildTargetGroup'),
				('BuildTarget','BuildTarget'),
				('DragAndDropVisualMode','DragAndDropVisualMode'),
				('DrawCameraMode','DrawCameraMode'),
				('EditorSkin','EditorSkin'),
				('ExportPackageOptions','ExportPackageOptions'),
				('FlashBuildSubtarget','FlashBuildSubtarget'),
				('FontRenderingMode','FontRenderingMode'),
				('FontTextureCase','FontTextureCase'),
				('GizmoType','GizmoType'),
				('ImportAssetOptions','ImportAssetOptions'),
				('InspectorMode','InspectorMode'),
				('LightmapBakeQuality','LightmapBakeQuality'),
				('MacFullscreenMode','MacFullscreenMode'),
				('MessageType','MessageType'),
				('ModelImporterAnimationCompression','ModelImporterAnimationCompression'),
				('ModelImporterAnimationType','ModelImporterAnimationType'),
				('ModelImporterGenerateAnimations','ModelImporterGenerateAnimations'),
				('ModelImporterMaterialName','ModelImporterMaterialName'),
				('ModelImporterMaterialSearch','ModelImporterMaterialSearch'),
				('ModelImporterMeshCompression','ModelImporterMeshCompression'),
				('ModelImporterTangentSpaceMode','ModelImporterTangentSpaceMode'),
				('MouseCursor','MouseCursor'),
				('PS3BuildSubtarget','PS3BuildSubtarget'),
				('PivotMode','PivotMode'),
				('PivotRotation','PivotRotation'),
				('PrefabType','PrefabType'),
				('ProceduralOutputType','ProceduralOutputType'),
				('RemoveAssetOptions','RemoveAssetOptions'),
				('ReplacePrefabOptions','ReplacePrefabOptions'),
				('ResolutionDialogSetting','ResolutionDialogSetting'),
				('ScriptCallOptimizationLevel','ScriptCallOptimizationLevel'),
				('SelectionMode','SelectionMode'),
				('SerializedPropertyType','SerializedPropertyType'),
				('StaticEditorFlags','StaticEditorFlags'),
				('StaticOcclusionCullingMode','StaticOcclusionCullingMode'),
				('StrippingLevel','StrippingLevel'),
				('TargetGlesGraphics','TargetGlesGraphics'),
				('TextureImporterFormat','TextureImporterFormat'),
				('TextureImporterGenerateCubemap','TextureImporterGenerateCubemap'),
				('TextureImporterMipFilter','TextureImporterMipFilter'),
				('TextureImporterNPOTScale','TextureImporterNPOTScale'),
				('TextureImporterNormalFilter','TextureImporterNormalFilter'),
				('TextureImporterType','TextureImporterType'),
				('Tool','Tool'),
				('UIOrientation','UIOrientation'),
				('ViewTool','ViewTool'),
				('WiiBuildDebugLevel','WiiBuildDebugLevel'),
				('WiiBuildSubtarget','WiiBuildSubtarget'),
				('WiiHio2Usage','WiiHio2Usage'),
				('WiiMemoryArea','WiiMemoryArea'),
				('WiiMemoryLabel','WiiMemoryLabel'),
				('WiiRegion','WiiRegion'),
				('XboxBuildSubtarget','XboxBuildSubtarget'),
				('XboxRunMethod','XboxRunMethod'),
				('iOSSdkVersion','iOSSdkVersion'),
				('iOSShowActivityIndicatorOnLoading','iOSShowActivityIndicatorOnLoading'),
				('iOSStatusBarStyle','iOSStatusBarStyle'),
				('iOSTargetDevice','iOSTargetDevice'),
				('iOSTargetOSVersion','iOSTargetOSVersion'),
				('iOSTargetResolution','iOSTargetResolution')
]

TREEEDITOR = [
				('FractalNoise','FractalNoise'),
				('Parlin','Parlin'),
				('RingLoop','RingLoop'),
				('SmoothRandom','SmoothRandom'),
				('SplineNode','SplineNode'),
				('TextureAtlas','TextureAtlas'),
				('TreeAOSphere','TreeAOSphere'),
				('TreeAttribute','Tree'),
				('TreeData','TreeData'),
				('TreeEditorHelper','TreeEditorHelper'),
				('TreeGroup','TreeGroup'),
				('TreeGroupBranch','TreeGroupBranch'),
				('TreeGroupLeaf','TreeGroupLeaf'),
				('TreeGroupRoot','TreeGroupRoot'),
				('TreeMaterial','TreeMaterial'),
				('TreeNode','TreeNode'),
				('TreeSpline','TreeSpline'),
				('TreeTriangle','TreeTriangle'),
				('TreeVertex','TreeVertex')
]

UNITYEDITOR_CALLBACKS = [
				('PostProcessBuildAttribute','PostProcessBuild'),
				('PostProcessSceneAttribute','PostProcessScene')
]

UNITYEDITOR_MACROS = [
				('MacroEvaluator','MacroEvaluator'),
				('MethodEvaluator','MethodEvaluator')
]

UNITYEDITOR_VISUALSTUDIOINTEGRATION = [
				('SolutionGuidGenerator','SolutionGuidGenerator')
]

UNITYEDITORINTERNAL = [
				('AnimationController','AnimationController'),
				('AssetStore','AssetStore'),
				('AssetStoreToolUtils','AssetStoreToolUtils'),
				('AvatorBodyMask','AvatorBodyMask'),
				('AvatorSkeletonMask','AvatorSkeletonMask'),
				('BlendTree','BlendTree'),
				('InternalEditorUtility','InternalEditorUtility'),
				('InternalGraphUtility','InternalGraphUtility'),
				('MacroEvents','MacroEvents'),
				('Macros','Macros'),
				('MacroWindow','MacroWindow'),
				('MonoScripts','MonoScripts'),
				('ProfilerDriver','ProfilerDriver'),
				('ProfilerProperty','ProfilerProperty'),
				('State','State'),
				('StateMachine','StateMachine'),
				('Transition','Transition'),
				# enum
				('AnimatorControllerEventType','AnimatorControllerEventType'),
				('AnimatorLayerBlendingMode','AnimatorLayerBlendingMode'),
				('ProfilerArea','ProfilerArea'),
				('ProfilerColumn','ProfilerColumn'),
				('ProfilerViewType','ProfilerViewType'),
				('TransitionConditionMode','TransitionConditionMode')
]